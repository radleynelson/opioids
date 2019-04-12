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
def drugs_list(request):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)


    #data = dmod.Triple.objects.select_related('opioids').values('opioids__drugname', 'opioids__isopioid').annotate(Sum('opioids_id'))
    data = dmod.Opioids.objects.values()
    drugs = list(data)

    
    return JsonResponse(drugs, safe=False)

@view_function
def drug(request, id:dmod.Opioids):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    d1 = dmod.Triple.objects.select_related('prescribers').filter(opioids = id).values('id','qty','prescribers__fname', 'prescribers__lname','opioids_id','prescribers__doctorid')[:10]
    o1 = dmod.Opioids.objects.filter(id = id.id).values()
    
    if not request.user.has_perm('admin.analytics'):
        d1 = []

    finalData = {
        'userList': list(d1),
        'drug': list(o1)
    }
    
    return JsonResponse(finalData, safe=False)

@view_function
def related_drugs(request, id:dmod.Opioids):
    
    url = "https://ussouthcentral.services.azureml.net/workspaces/4718f244148842c4b087009708bf0c75/services/21265032cea24fb58ad264e6d96415e4/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\n  \"Inputs\": {\n    \"input1\": {\n      \"ColumnNames\": [\n        \"opioids_id\"\n      ],\n      \"Values\": [\n        [\n          \" 3\"\n        ]\n      ]\n    }\n  }\n}"
    headers = {
        'Authorization': "Bearer sfVcw2RU1e4hobI/iZKhJer760t3fB6u1y/ZzcyHzLShf3CKzitss/q8Aqjn12Z27MBqVduG2pVwFb0KHNLnDg==",
        'Content-Type': "application/json",
        'Access-Control-Allow-Origin': "*",
        'cache-control': "no-cache",
        'Postman-Token': "cbbbbf1c-4b55-475f-a989-934334c726c6"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    
    responseData = json.loads(response.text);

    itemsList = responseData['Results']['output1']['value']['Values'][0]

    drugs = dmod.Opioids.objects.filter(pk__in=(itemsList)).values()
    
    return JsonResponse(list(drugs), safe=False)


