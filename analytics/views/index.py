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
from decimal import Decimal
from django.http import HttpResponseRedirect


@login_required(login_url='/account')
@view_function
def process_request(request):
    if not request.user.has_perm('admin.dashboard'):
        return HttpResponseRedirect('/', request.user)


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
def getOpioids(request):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.dashboard'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    drugs = dmod.Triple.objects.select_related('opioids').filter(opioids__isopioid = 1).values('opioids__drugname', 'opioids__isopioid').annotate(Sum('qty')).order_by('-qty__sum')

    
    return JsonResponse(list(drugs), safe=False)

@view_function
def getTop50Prescribers(request):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.dashboard'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    p = dmod.Prescribers.objects.all().order_by('-numberofopioidsprescribed').values()[:50]

    
    return JsonResponse(list(p), safe=False)


@view_function
def getOpioidsPrescribed(request, id:dmod.Prescribers):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.dashboard'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    p = dmod.Triple.objects.select_related('opioids','prescribers').filter(prescribers = id, opioids__isopioid = 1).values('opioids__drugname', 'prescribers__totalprescriptions').annotate(Sum('qty'))

    
    return JsonResponse(list(p), safe=False)

@view_function
def getTopSpecialtiesToalOpioids(request):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.dashboard'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    p = dmod.Triple.objects.select_related('opioids','prescribers').select_related('prescribers__specialties').filter(opioids__isopioid = 1).values('prescribers__specialties__specialty').annotate(Sum('qty')).order_by('-qty__sum')[:5]

    
    return JsonResponse(list(p), safe=False)

@view_function
def getTopStates(request):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.dashboard'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    p = dmod.Overdoses.objects.all().values().order_by('-percent')[:5]

    
    return JsonResponse(list(p), safe=False)

@view_function
def getSpider(request, doctor:dmod.Prescribers, doctor2:dmod.Prescribers):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.dashboard'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    state = dmod.Overdoses.objects.get(id = doctor.overdoses_id)

    state2 = dmod.Overdoses.objects.get(id = doctor2.overdoses_id)

    print(state.percent)

    retrunValue = {
        'risk-rank': doctor.risk_rank,
        'percent': ((doctor.numberofopioidsprescribed/doctor.totalprescriptions) * 100),
        'state-percent': state.percent * 3000,
        'doctorid': doctor.doctorid,
        'risk-rank2': doctor2.risk_rank,
        'percent2': ((doctor2.numberofopioidsprescribed/doctor2.totalprescriptions) * 100),
        'state-percent2': state2.percent * 3000,
        'doctorid2': doctor2.doctorid
    }

    
    return JsonResponse(retrunValue, safe=False)

@view_function
def getkpis(request):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    if not request.user.has_perm('admin.dashboard'):
        return JsonResponse('You do not have sufficient rights to access this content', safe=False)

    k1 = dmod.Triple.objects.select_related('opioids').values('opioids__isopioid').annotate(Sum('qty'))

    k1list = list(k1)

    k2 = dmod.Prescribers.objects.filter(risk_rank=100).count()

    k3 = dmod.BatchStatistics.objects.latest()

    k5 = dmod.Prescribers.objects.filter(risk_rank__gt = k3.upperbound).count()


    retrunValue = {
        'opioid_ratio':  round((k1list[1]['qty__sum'] / k1list[0]['qty__sum']) * 100, 2),
        'only_prescribing_opioids': k2,
        'mean_risk_rank': round(k3.mean,2),
        'upper_bound_risk_rank': k3.upperbound,
        'prescribers_at_risk': k5

    }

    
    return JsonResponse(retrunValue, safe=False)