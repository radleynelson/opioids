# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554679569.832014
_enable_loop = True
_template_filename = '/Users/Rad/Desktop/Intex2/intex2/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>DMP</title>\n\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n\n        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>\n\n    </head>\n    <body>\n\n        <header>\n            <nav class="navbar navbar-expand-lg navbar-light bg-light">\n                <div class="container">\n                  <a class="navbar-brand" href="#">Group 2-13 Intex</a>\n                  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\n                  <span class="navbar-toggler-icon"></span>\n                </button>\n              \n                  <div class="collapse navbar-collapse" id="navbarSupportedContent">\n                    <ul class="navbar-nav ml-auto">\n                        <li class="nav-item">\n                            <a class="nav-link" href="#">Contact</a>\n                        </li>\n                        <li class="nav-item">\n                            <a class="nav-link" href="#">About</a>\n                        </li>\n')
        if request.user.is_superuser:
            __M_writer('                            <li class="nav-item">\n                                <a class="nav-link" href="#">Dashboard</a>\n                            </li>\n')
        if not request.user.is_authenticated:
            __M_writer('                            <li class="nav-item dropdown">\n                                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n                                    Account\n                                </a>\n                                <!-- Here\'s the magic. Add the .animate and .slide-in classes to your .dropdown-menu and you\'re all set! -->\n                                <div class="dropdown-menu dropdown-menu-right animate slideIn" aria-labelledby="navbarDropdown">\n                                <a class="dropdown-item" href="/account">Login</a>\n                                <a class="dropdown-item" href="/account/signup">Sign Up</a>\n                                <div class="dropdown-divider"></div>\n                                <a class="dropdown-item" href="#">Learn More</a>\n                                </div>\n                            </li>\n')
        else:
            __M_writer('                        <li class="nav-item dropdown">\n                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n                                Welcome ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( request.user.username))
            __M_writer('\n                            </a>\n                            <!-- Here\'s the magic. Add the .animate and .slide-in classes to your .dropdown-menu and you\'re all set! -->\n                            <div class="dropdown-menu dropdown-menu-right animate slideIn" aria-labelledby="navbarDropdown">\n                            <a class="dropdown-item" href="/account/logout">Logout</a>\n                        </li>\n')
        __M_writer('                    </ul>\n                  </div>\n                </div>\n              </nav>\n        </header>\n\n        <main style="width: 100%; padding-left: 0; padding-right: 0;">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </main>\n\n        <footer>\n            <div><a href="http://django-mako-plus.readthedocs.io/">Online Documentation</a></div>\n            <div><a href="https://github.com/doconix/django-mako-plus/">DMP on GitHub</a></div>\n        </footer>\n\n    </body>\n</html>\n')
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
{"filename": "/Users/Rad/Desktop/Intex2/intex2/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "27": 2, "28": 10, "29": 13, "30": 14, "31": 14, "32": 38, "33": 39, "34": 43, "35": 44, "36": 56, "37": 57, "38": 59, "39": 59, "40": 66, "45": 75, "51": 73, "57": 73, "63": 57}}
__M_END_METADATA
"""
