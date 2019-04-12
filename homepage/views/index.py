from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from account import models as amod

@view_function
def process_request(request, user:amod.User = None):
    utc_time = datetime.utcnow()

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
        # sent to index.html:
        'utc_time': utc_time,
        'user': username,
        # sent to index.html and index.js:
        jscontext('data'): {
            'showMessage': showMessage,
            'pageMessage': pageMessage,
            'user': username,
            'permissions': userPermissions
        }
    }
    return request.dmp.render('index.html', context)


    