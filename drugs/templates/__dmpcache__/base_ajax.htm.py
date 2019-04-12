# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554752937.068361
_enable_loop = True
_template_filename = '/Users/Rad/Desktop/Intex2/intex2/drugs/templates/base_ajax.htm'
_template_uri = 'base_ajax.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    Sub-templates should place their ajax content here.\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Rad/Desktop/Intex2/intex2/drugs/templates/base_ajax.htm", "uri": "base_ajax.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "26": 3, "27": 5, "28": 5, "33": 10, "39": 8, "45": 8, "51": 45}}
__M_END_METADATA
"""
