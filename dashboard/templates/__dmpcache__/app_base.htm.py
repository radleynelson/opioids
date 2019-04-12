# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554697770.783247
_enable_loop = True
_template_filename = '/Users/Rad/Desktop/Intex2/intex2/dashboard/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>Dashboard</title>\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n        <link rel="stylesheet" href="/path/to/material-icons/iconfont/material-icons.css">\n        <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic">\n        <link rel="stylesheet" href="//fonts.googleapis.com/icon?family=Material+Icons">\n        <link href="https://use.fontawesome.com/releases/v5.0.8/css/all.css" rel="stylesheet">\n\n\n    </head>\n    <body>\n\n\n        <main>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </main>\n\n        <footer>\n        </footer>\n\n    </body>\n</html>\n')
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
{"filename": "/Users/Rad/Desktop/Intex2/intex2/dashboard/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "26": 2, "27": 10, "28": 11, "29": 11, "34": 25, "40": 23, "46": 23, "52": 46}}
__M_END_METADATA
"""
