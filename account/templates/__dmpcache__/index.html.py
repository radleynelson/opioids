# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554671127.547293
_enable_loop = True
_template_filename = '/Users/Rad/Desktop/Intex2/intex2/account/templates/index.html'
_template_uri = 'index.html'
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
        

        __M_writer('\n')
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
        __M_writer('\n    <div class="content">\n        <!-- <div id="alignLeft">\n            <div class="container text-center">\n                <form method="POST" class="form-signin">\n                    ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( csrf_input ))
        __M_writer('\n                    <img class="mb-4" src="https://getbootstrap.com/docs/4.1/assets/brand/bootstrap-solid.svg alt="" width="72" height="72">\n                    <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>\n                    <label for="id_Username" class="sr-only">User Name</label>\n                    <input type="text" name="Username" required="" id="id_Username" class="form-control" placeholder="User Name" required="" autofocus="">\n                    <label for="id_Password" class="sr-only">Password</label>\n                    <input type="password" name="Password" maxlength="32" required="" id="id_Password" class="form-control" placeholder="Password" required="">\n                    <br>\n                    <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>\n                    <p class="mt-5 mb-3 text-muted">© 2019</p>\n                </form>\n            </div>\n        </div> -->\n        <div class="container py-5">\n                <div class="row">\n                    <div class="col-md-12">\n                        <h2 class="text-center text-white mb-4">Bootstrap 4 Login Form</h2>\n                        <div class="row">\n                            <div class="col-md-6 mx-auto">\n            \n                                <!-- form card login -->\n                                <div class="card rounded-0">\n                                    <div class="card-header">\n                                        <h3 class="mb-0">Login</h3>\n                                    </div>\n                                    <div class="card-body">\n                                        <form class="form" role="form" autocomplete="off" id="formLogin" novalidate="" method="POST">\n                                            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( csrf_input ))
        __M_writer('\n                                            <div class="form-group">\n                                                    <label for="id_Username" class="sr-only">User Name</label>\n                                                    <input type="text" name="Username" required="" id="id_Username" class="form-control" placeholder="User Name" required="" autofocus="">\n                                                <div class="invalid-feedback">Oops, you missed this one.</div>\n                                            </div>\n                                            <div class="form-group">\n                                                    <label for="id_Password" class="sr-only">Password</label>\n                                                    <input type="password" name="Password" maxlength="32" required="" id="id_Password" class="form-control" placeholder="Password" required="">\n                                                <div class="invalid-feedback">Enter your password too!</div>\n                                            </div>\n                                            <div>\n                                                <label class="custom-control custom-checkbox">\n                                                  <input type="checkbox" class="custom-control-input">\n                                                  <span class="custom-control-indicator"></span>\n                                                </label>\n                                            </div>\n                                            <button type="submit" class="btn btn-success btn-lg float-right" id="btnLogin">Login</button>\n                                        </form>\n                                    </div>\n                                    <!--/card-block-->\n                                </div>\n                                <!-- /form card login -->\n            \n                            </div>\n            \n            \n                        </div>\n                        <!--/row-->\n            \n                    </div>\n                    <!--/col-->\n                </div>\n                <!--/row-->\n            </div>\n            <!--/container-->\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Rad/Desktop/Intex2/intex2/account/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 72, "49": 3, "57": 3, "58": 8, "59": 8, "60": 35, "61": 35, "67": 61}}
__M_END_METADATA
"""
