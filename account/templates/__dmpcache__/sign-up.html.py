# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554670439.421655
_enable_loop = True
_template_filename = '/Users/Rad/Desktop/Intex2/intex2/account/templates/sign-up.html'
_template_uri = 'sign-up.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context)
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n        <div class="container-fluid bg-light py-3">\n            <div class="row">\n                <div class="col-md-6 mx-auto">\n                    <div class="card card-body">\n                        <h3 class="text-center mb-4">Sign-up</h3>\n                        <div class="alert alert-danger">\n                            <a class="close font-weight-light" data-dismiss="alert" href="#">×</a>Password is too short.\n                        </div>\n                        <form method="POST">\n                            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( csrf_input ))
        __M_writer('\n                            <div class="form-group has-success">\n                                <input type="text" name="username" maxlength="150" autofocus="" required="" id="id_username" class="form-control input-lg" placeholder="User Name">\n                            </div>\n                            <div class="form-group has-success">\n                                <input type="email" name="email" maxlength="254" id="id_email" class="form-control input-lg" placeholder="Email" />\n                            </div>\n                            <div class="form-group has-success">\n                                <input type="password" name="password1" required="" id="id_password1" aria-autocomplete="list" class="form-control input-lg" placeholder="Password">\n                            </div>\n                            <div class="form-group has-success">\n                                <input type="password" name="password2" required="" id="id_password2" class="form-control input-lg" placeholder="Confirm Password">\n                            </div>\n                            <div class="form-group">\n                                <select class="form-control input-lg">\n                                    <option selecterd="">Sequrity Question</option>\n                                </select>\n                            </div>\n                            <div class="form-group">\n                                <input class="form-control input-lg" placeholder="Sequrity Answer" name="answer" value="" type="text">\n                            </div>\n                            <div class="checkbox">\n                                <label class="small">\n                                    <input name="terms" type="checkbox">I have read and agree to the <a href="#">terms of service</a>\n                                </label>\n                            </div>\n                            <input class="btn btn-lg btn-primary btn-block" value="Sign Me Up" type="submit">\n                        </form>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Rad/Desktop/Intex2/intex2/account/templates/sign-up.html", "uri": "sign-up.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 47, "49": 3, "57": 3, "58": 14, "59": 14, "65": 59}}
__M_END_METADATA
"""
