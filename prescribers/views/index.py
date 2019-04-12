from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from drugs import models as dmod
from django.db.models import Sum
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
import requests
import json

@login_required(login_url='/account')
@view_function
def process_request(request):

    username = str(request.user.username)
    pageMessage = ''
    showMessage = False

    userPermissions = []

    if(request.user is not None):
        userPermissions = list(request.user.get_all_permissions())

    try:
        pageMessage = request.session['pageMessage']
    except:
        pageMessage = ''

    try:
        showMessage = request.session['showMessage']
    except:
        showMessage = False

    request.session['showMessage'] = False
    request.session['pageMessage'] = ''

    context = {
        # sent to index.html and index.js:
        jscontext('data'): {
            'showMessage': showMessage,
            'pageMessage': pageMessage,
            'user': username,
            'permissions': userPermissions,
        }
    }

    return request.dmp.render('index.html', context)

@view_function
def prescribers_list(request):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    prescribers = dmod.Prescribers.objects.select_related('overdoses', 'specialties').all().values('id', 'doctorid','fname','lname','gender','overdoses__abbrev','credentials','risk_rank','isoutlier','totalprescriptions','numberofopioidsprescribed','specialties__specialty')

    data = list(prescribers)


    return JsonResponse(data, safe=False)

@view_function
def prescriber(request, id:dmod.Prescribers):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    queryset = dmod.Prescribers.objects.select_related('specialties','overdoses').filter(id = id.id)
    p1 = queryset.values('gender','opioid_prescriber','risk_rank','isoutlier','overdoses__abbrev','specialties__specialty')
    p2 = queryset.values('id','doctorid','fname','lname','credentials','totalprescriptions','numberofopioidsprescribed')
    drugList = dmod.Triple.objects.select_related('opioids').filter(prescribers = id).values('qty', 'opioids__drugname','opioids__isopioid', 'opioids__id', 'opioids__risk_score').order_by('-qty')


    data = list(p1)
    dataLeft=list(p2)
    drugs = list(drugList)

    if not request.user.has_perm('admin.analytics'):
        drugs = []

    PrescriberDrugs = {
        'PrescriberData': data,
        'PrescriberDataLeft': dataLeft,
        'drugs': drugs,
    }
    

    return JsonResponse(PrescriberDrugs, safe=False)

@view_function
def related_prescribers(request, prescriber:dmod.Prescribers):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.analytics'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    url = "https://ussouthcentral.services.azureml.net/workspaces/4718f244148842c4b087009708bf0c75/services/80172f96647a4920ac62a8846b54af6b/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\n  \"Inputs\": {\n    \"input1\": {\n      \"ColumnNames\": [\n        \"prescribers_id\"\n      ],\n      \"Values\": [\n        [\n          \"3\"\n        ]\n      ]\n    }\n  }\n}"
    headers = {
        'Authorization': "Bearer /yRI//Z+u2bgaYzHCA2PqqbJgNdC/orSTRJ2a7rb8U4e0DDFTDzncKfhp30KqfUEHTqU4cr1ZoNGTWYnTk70gg==",
        'Content-Type': "application/json",
        'Access-Control-Allow-Origin': "*",
        'cache-control': "no-cache",
        'Postman-Token': "3d4030b8-c09b-464f-8286-ff8aacce9ffa"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    responseData = json.loads(response.text);

    itemsList = responseData['Results']['output1']['value']['Values'][0]

    prescribers = dmod.Prescribers.objects.filter(pk__in=(itemsList)).values()

    data = []

    for x in prescribers:
        user = {
            'userInfo': x,
            'Top5Drugs': list(dmod.Triple.objects.select_related('opioids').filter(prescribers = x['id']).values('qty', 'opioids__drugname','opioids__isopioid', 'opioids__id').order_by('-qty')[:5])
        }
        data.append(user)

    return JsonResponse(data, safe=False)


@view_function
def edit_prescriber(request, prescriber:dmod.Prescribers):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.crud'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)
    p1 = dmod.Prescribers.objects.filter(id=prescriber.id).values()

    return JsonResponse(list(p1), safe=False)

@view_function
def update_prescriber(request, prescriber:dmod.Prescribers = None):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.method == 'POST':
        return JsonResponse('Please Send Post Data', safe=False)

    if not request.user.has_perm('admin.crud'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    print(request.body)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['fname']
    if prescriber is None:
        p1 = dmod.Prescribers()
    else:
        p1 = dmod.Prescribers.objects.filter(id=prescriber.id).first()

    p1.fname = body['fname']
    p1.lname = body['lname']
    p1.credentials = body['credentials']
    p1.opioid_prescriber = body['opioid_prescriber']
    p1.numberofopioidsprescribed = body['numberofopioidsprescribed']
    p1.overdoses = dmod.Overdoses.objects.get(id=body['overdoses_id'])
    p1.specialties = dmod.Specialties.objects.get(id=body['specialties_id'])
    p1.doctorid = body['doctorid']
    p1.gender = body['gender']
    p1.totalprescriptions = body['totalprescriptions']
    p1.save()

    return JsonResponse("Saved Successfully", safe=False)


@view_function
def delete_prescriber(request, prescriber:dmod.Prescribers):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.crud'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    if prescriber is None:
        JsonResponse("Not Foud for Deletion", safe=False)
    else:
        p1 = dmod.Prescribers.objects.filter(id=prescriber.id).first()
        p1.delete()

    
    return JsonResponse("Deleted Successfully Successfully", safe=False)


@view_function
def drug_reccomender(request, prescriber:dmod.Prescribers, itemid:str):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.analytics'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    url = "https://ussouthcentral.services.azureml.net/workspaces/4718f244148842c4b087009708bf0c75/services/f2f2d674641f44a4ae5d8e214cb96e2b/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\n  \"Inputs\": {\n    \"input1\": {\n      \"ColumnNames\": [\n        \"prescribers_id\",\n        \"opioids_id\"\n      ],\n      \"Values\": [\n        [\n          \"" + str(prescriber.id) + "\",\n          \"" + itemid + "\"\n        ]\n      ]\n    }\n  }\n}"
    headers = {
        'Authorization': "Bearer Esk2DjqiLohYeWisLD1iNhfzgaYVxxfwm9YalFHWVDGQwxjTanxSCXWhofCLD1KLpIA+1g2akJLl4ELbXZyonA==",
        'Content-Type': "application/json",
        'Access-Control-Allow-Origin': "*",
        'cache-control': "no-cache",
        'Postman-Token': "c3d107fe-cb93-4e77-b726-36ff79d998f6"
        }


    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    responseData = json.loads(response.text);

    itemsList = responseData['Results']['output1']['value']['Values'][0]

    d = []
    print()
    print()
    print()
    print()
    print(itemsList)
    print()
    print()
    print()
    print()

    for x in itemsList:
        tempdrug = dmod.Opioids.objects.filter(id = x).values()
        t = list(tempdrug)
        if t[0]['isopioid'] == 0:
            d.append(t[0])

    #drugs = dmod.Opioids.objects.filter(pk__in=(itemsList), isopioid = 1).values().order_by

    print()
    print()
    print()
    print(d)
    print()
    print()
    print()
    print()

    return JsonResponse(d[:5], safe=False)



