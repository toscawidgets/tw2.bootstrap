"""
``tw2.bootstrap`` provides the same widgets as ``tw2.forms`` enabled to
work with `twitter bootstrap <http://twitter.github.com/bootstrap/>`_.
"""

import tw2.core as twc
import tw2.forms as twf
import tw2.jquery as twj

__all__ = [
    'bootstrap_css',
    'bootstrap_responsive_css',
    'bootstrap_js',

    'Bootstrap',

    'InputField',
    'TextField',
    'TextArea',
    'CheckBox',
    'RadioButton',
    'PasswordField',
    'FileField',
    'HiddenField',
    'IgnoredField',
    'LabelField',
    'LinkField',
    'Button',
    'SubmitButton',
    'ResetButton',
    'HorizontalLayout',
    'HorizontalForm',

    'CalendarDatePicker',
    'CalendarDateTimePicker',
    'CheckBoxList',
    'CheckBoxTable',

    'DataGrid',

    'FieldSet',
    'Form',
    'FormPage',

    'GridLayout',

    'ImageButton',

    'Label',
    'ListFieldSet',
    'ListForm',
    'ListLayout',

    'MultipleSelectField',
    'MultipleSelectionField',

    'PostlabeledCheckBox',
    'PostlabeledPartialRadioButton',

    'RadioButtonList',
    'RadioButtonTable',
    'RowLayout',

    'SelectionField',
    'SeparatedCheckBoxTable',
    'SeparatedRadioButtonTable',
    'SingleSelectField',
    'Spacer',

    'TableFieldSet',
    'TableForm',
    'TableLayout',

    'VerticalCheckBoxTable',
    'VerticalRadioButtonTable',
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


class _BoolControl(Bootstrap):
    template = "tw2.bootstrap.templates.bool_control"

    def prepare(self):
        super(_BoolControl, self).prepare()
        self.safe_modify('attrs')
        del self.attrs['class']


class CheckBox(_BoolControl, twf.CheckBox):
    css_class = "checkbox"


class RadioButton(_BoolControl, twf.RadioButton):
    css_class = "radio"


class PasswordField(InputField, twf.PasswordField):
    pass


class FileField(Bootstrap, twf.FileField):
    css_class = "input-file"


class HiddenField(twf.HiddenField):
    pass


class IgnoredField(twf.HiddenField):
    pass


class LabelField(Bootstrap, twf.LabelField):
    template = "tw2.bootstrap.templates.label_field"
    css_class = "input-medium uneditable-input"

    def prepare(self):
        super(LabelField, self).prepare()
        self.safe_modify('attrs')
        del self.attrs['class']


class LinkField(Bootstrap, twf.LinkField):
    """ TODO -- not sure how to take this one on.

    It doesn't seem to nicely fit the bootstrap paradigm.  Do you have
    any ideas?
    """
    pass


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


class HorizontalForm(Bootstrap, twf.Form):
    """Equivalent to a Form containing a HorizontalLayout."""
    template = "mako:tw2.bootstrap.templates.horizontal_form"
    css_class = "form-horizontal"
    child = twc.Variable(default=HorizontalLayout)
    children = twc.Required
    submit = SubmitButton(id='submit', value='Save')

    legend = twc.Param('Legend text for the form.', '')


class CalendarDatePicker(Bootstrap, twf.CalendarDatePicker):
    pass


class CalendarDateTimePicker(Bootstrap, twf.CalendarDateTimePicker):
    pass


class CheckBoxList(Bootstrap, twf.CheckBoxList):
    pass


class CheckBoxTable(Bootstrap, twf.CheckBoxTable):
    pass


class DataGrid(Bootstrap, twf.DataGrid):
    pass


class FieldSet(Bootstrap, twf.FieldSet):
    pass


class Form(Bootstrap, twf.Form):
    pass


class FormPage(Bootstrap, twf.FormPage):
    pass


class GridLayout(Bootstrap, twf.GridLayout):
    pass


class ImageButton(Bootstrap, twf.ImageButton):
    pass


class Label(Bootstrap, twf.Label):
    pass


class ListFieldSet(Bootstrap, twf.ListFieldSet):
    pass


class ListForm(Bootstrap, twf.ListForm):
    pass


class ListLayout(Bootstrap, twf.ListLayout):
    pass


class MultipleSelectField(Bootstrap, twf.MultipleSelectField):
    pass


class MultipleSelectionField(Bootstrap, twf.MultipleSelectionField):
    pass


class PostlabeledCheckBox(Bootstrap, twf.PostlabeledCheckBox):
    pass


class PostlabeledPartialRadioButton(Bootstrap,
                                    twf.PostlabeledPartialRadioButton):
    pass


class RadioButtonList(Bootstrap, twf.RadioButtonList):
    pass


class RadioButtonTable(Bootstrap, twf.RadioButtonTable):
    pass


class RowLayout(Bootstrap, twf.RowLayout):
    pass


class SelectionField(Bootstrap, twf.SelectionField):
    pass


class SeparatedCheckBoxTable(Bootstrap, twf.SeparatedCheckBoxTable):
    pass


class SeparatedRadioButtonTable(Bootstrap, twf.SeparatedRadioButtonTable):
    pass


class SingleSelectField(Bootstrap, twf.SingleSelectField):
    pass


class Spacer(Bootstrap, twf.Spacer):
    template = "tw2.bootstrap.templates.spacer"


class TableFieldSet(Bootstrap, twf.TableFieldSet):
    pass


class TableForm(Bootstrap, twf.TableForm):
    pass


class TableLayout(Bootstrap, twf.TableLayout):
    pass


class VerticalCheckBoxTable(Bootstrap, twf.VerticalCheckBoxTable):
    pass


class VerticalRadioButtonTable(Bootstrap, twf.VerticalRadioButtonTable):
    pass
