# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555071034.6759858
_enable_loop = True
_template_filename = '/Users/Rad/Desktop/Intex2/intex2/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


from drugs import models as dmod 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>HHS Opioid Analytics</title>\n\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n\n        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>\n        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">\n        <link\n        type="text/css"\n        rel="stylesheet"\n        href="//unpkg.com/bootstrap-vue@latest/dist/bootstrap-vue.min.css"\n        />\n\n\n    </head>\n    <body>\n\n        <header>\n            <nav class="navbar navbar-expand-lg navbar-light bg-light">\n                <div class="container">\n                  <a class="navbar-brand" href="#"><img height="50" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/logo4.png"/></a>\n                  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\n                  <span class="navbar-toggler-icon"></span>\n                </button>\n              \n                  <div class="collapse navbar-collapse" id="navbarSupportedContent">\n                    <ul class="navbar-nav ml-auto">\n                        <li class="nav-item">\n                            <a href="/drugs" class="nav-link" href="#">Drugs</a>\n                        </li>\n                        <li class="nav-item">\n                            <a href="/prescribers" class="nav-link" href="#">Prescribers</a>\n                        </li>\n                        ')
        __M_writer('\n')
        if request.user.has_perm('admin.dashboard'):
            __M_writer('                            <li class="nav-item">\n                                <a class="nav-link" href="/analytics">Dashboard</a>\n                            </li>\n')
        if not request.user.is_authenticated:
            __M_writer('                            <li class="nav-item dropdown">\n                                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n                                    Account\n                                </a>\n                                <!-- Here\'s the magic. Add the .animate and .slide-in classes to your .dropdown-menu and you\'re all set! -->\n                                <div class="dropdown-menu dropdown-menu-right animate slideIn" aria-labelledby="navbarDropdown">\n                                <a class="dropdown-item" href="/account">Login</a>\n                                <a class="dropdown-item" href="/account/signup">Sign Up</a>\n                                \n                            </li>\n')
        else:
            __M_writer('                        <li class="nav-item dropdown">\n                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n                                Welcome ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( request.user.username))
            __M_writer('\n                            </a>\n                            <!-- Here\'s the magic. Add the .animate and .slide-in classes to your .dropdown-menu and you\'re all set! -->\n                            <div class="dropdown-menu dropdown-menu-right animate slideIn" aria-labelledby="navbarDropdown">\n                            <a class="dropdown-item" href="/account/logout">Logout</a>\n')
            if request.user.has_perm('admin.analytics') and not request.user.has_perm('admin.see_names'):
                __M_writer('                                ')
 
                p = dmod.Prescribers.objects.filter(doctorid = request.user.username).first()
                pid = p.id
                                                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['pid','p'] if __M_key in __M_locals_builtin_stored]))
                __M_writer('\n                                <div class="dropdown-divider"></div>\n                                    <a class="dropdown-item" href="/prescribers#/items/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(pid))
                __M_writer('">My Profile</a>\n                                </div>\n')
            __M_writer('\n                            </div>\n                            \n                        </li>\n')
        __M_writer('                    </ul>\n                  </div>\n                </div>\n              </nav>\n        </header>\n\n        <main style="width: 100%; padding-left: 0; padding-right: 0;">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </main>\n\n        <!-- Footer -->\n        <footer class="page-footer font-small cyan darken-3">\n\n        <!-- Footer Elements -->\n        <div class="container">\n        \n            <!-- Grid row-->\n            <div class="row">\n        \n                <!-- Grid column -->\n                <div class="col-md-12 py-5">\n                    <div class="mb-5 flex-center">\n        \n                        <a class="fb-ic">\n                            <i class="fab fa-microsoft white-text mr-md-5 mr-3 fa-2x"></i>\n                        </a>\n                        <a class="tw-ic">\n                            <i class="fab fa-vuejs white-text mr-md-5 mr-3 fa-2x"></i>\n                        </a>\n                        <a class="gplus-ic">\n                            <i class="fab fa-python white-text mr-md-5 mr-3 fa-2x"></i>\n                        </a>\n                        <a class="gplus-ic">\n                            <i class="fas fa-file-medical white-text mr-md-5 mr-3 fa-2x"></i>\n                        </a>\n                        <a class="gplus-ic">\n                            <i class="fas fa-chart-bar white-text mr-md-5 mr-3 fa-2x"></i>\n                        </a>\n\n                        \n                        \n                    </div>\n                </div>\n                <!-- Grid column -->\n        \n            </div>\n            <!-- Grid row-->\n        \n        </div>\n            <!-- Footer Elements -->\n        \n            <!-- Copyright -->\n        <div class="footer-copyright text-center py-3">© 2019 Copyright:\n            <a href="https://www.is-celebrities-consulting.com">is-celebrities-consulting.com</a>\n        </div>\n            <!-- Copyright -->\n    \n      </footer>\n      <!-- Footer -->\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n                Site content goes here in sub-templates.\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Rad/Desktop/Intex2/intex2/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 45, "20": 0, "30": 2, "31": 10, "32": 13, "33": 14, "34": 14, "35": 32, "36": 32, "37": 45, "38": 46, "39": 47, "40": 51, "41": 52, "42": 62, "43": 63, "44": 65, "45": 65, "46": 70, "47": 71, "48": 71, "55": 74, "56": 76, "57": 76, "58": 79, "59": 84, "64": 93, "70": 91, "76": 91, "82": 76}}
__M_END_METADATA
"""
