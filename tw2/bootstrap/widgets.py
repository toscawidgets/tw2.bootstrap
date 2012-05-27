import tw2.core as twc
import tw2.forms as twf
import tw2.jquery as twj

__all__ = [
    'bootstrap_css',
    'bootstrap_responsive_css',
    'bootstrap_js',
    'Button',
    'SubmitButton',
    'ResetButton',
    'HorizontalLayout',
    'HorizontalForm',
]


bootstrap_css = twc.CSSLink(
    filename='static/css/bootstrap.css')
bootstrap_responsive_css = twc.CSSLink(
    filename='static/css/bootstrap-responsive.css')
bootstrap_js = twc.JSLink(
    filename='static/js/bootstrap.js',
    resources=[twj.jquery_js])


class Bootstrap(twc.Widget):
    """ Abstract base class for tw2.bootstrap widgets. """

    #template = "genshi:tw2.bootstrap.templates.bootstrap"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        #bootstrap_js,
        bootstrap_css, bootstrap_responsive_css,
    ]

#    @classmethod
#    def post_define(cls):
#        pass
#        # put custom initialisation code here
#
#    def prepare(self):
#        super(Bootstrap, self).prepare()
#        # put code here to run just before the widget is displayed


class InputField(Bootstrap, twf.InputField):
    css_class = 'input-medium'


class TextField(InputField, twf.TextField):
    pass


class TextArea(Bootstrap, twf.TextArea):
    css_class = 'input-xlarge'


class Button(Bootstrap, twf.Button):
    css_class = 'btn'


class SubmitButton(Button, twf.SubmitButton):
    css_class = 'btn btn-primary'


class ResetButton(Button, twf.ResetButton):
    pass


class HorizontalLayout(Bootstrap, twf.widgets.BaseLayout):
    __doc__ = """
    Arrange widgets and labels horizontally:
    Float left, right-aligned labels on same line as controls
    """ + twf.widgets.BaseLayout.__doc__
    template = "mako:tw2.bootstrap.templates.horizontal_layout"


class HorizontalForm(Bootstrap, twf.widgets.Form):
    """Equivalent to a Form containing a HorizontalLayout."""
    template = "mako:tw2.bootstrap.templates.horizontal_form"
    css_class = "form-horizontal"
    child = twc.Variable(default=HorizontalLayout)
    children = twc.Required
    submit = SubmitButton(id='submit', value='Save')

    legend = twc.Param('Legend text for the form.', '')
