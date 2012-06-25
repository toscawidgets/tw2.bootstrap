"""
``tw2.bootstrap.forms`` is a drop-in replacement for ``tw2.forms`` enabled to
work with `twitter bootstrap <http://twitter.github.com/bootstrap/>`_.
"""

import tw2.core as twc
import tw2.forms as twf
import tw2.jquery as twj

from datetime import datetime
from tw2.bootstrap.forms.utils import replace_all

__all__ = [
    'bootstrap_css',
    'bootstrap_responsive_css',
    'bootstrap_js',

    'BootstrapMixin',

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
    'CalendarTimePicker',
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


bootstrap_img = twc.DirLink(
    modname=__name__,
    filename='static/bootstrap/img')
bootstrap_css = twc.CSSLink(
    modname=__name__,
    filename='static/bootstrap/css/bootstrap.css',
    resources=[bootstrap_img])
bootstrap_responsive_css = twc.CSSLink(
    modname=__name__,
    filename='static/bootstrap/css/bootstrap-responsive.css')
bootstrap_js = twc.JSLink(
    modname=__name__,
    filename='static/bootstrap/js/bootstrap.js',
    resources=[twj.jquery_js],
    location='headbottom')

datepicker_img = twc.DirLink(
    modname=__name__,
    filename='static/datepicker/img')
datepicker_css = twc.CSSLink(
    modname=__name__,
    filename='static/datepicker/css/datepicker.css',
    resources=[bootstrap_css, datepicker_img])
datepicker_js = twc.JSLink(
    modname=__name__,
    filename='static/datepicker/js/bootstrap-datepicker.js',
    resources=[bootstrap_js],
    location='headbottom')

timepicker_css = twc.CSSLink(
    modname=__name__,
    filename='static/timepicker/css/timepicker.css',
    resources=[bootstrap_css])
timepicker_js = twc.JSLink(
    modname=__name__,
    filename='static/timepicker/js/bootstrap-timepicker.js',
    resources=[bootstrap_js],
    location='headbottom')


class BootstrapMixin(twc.Widget):
    """ Abstract base class for tw2.bootstrap.forms widgets. """

    #template = "genshi:tw2.bootstrap.forms.templates.bootstrap"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        #bootstrap_js,
        bootstrap_css, bootstrap_responsive_css,
    ]

    selector = twc.Variable("Escaped id.  jQuery selector.")

#    @classmethod
#    def post_define(cls):
#        pass
#        # put custom initialisation code here
#
    def prepare(self):
        super(BootstrapMixin, self).prepare()
        if 'id' in self.attrs:
            self.selector = "#" + self.attrs['id'].replace(':', '\\:')


class InputField(BootstrapMixin, twf.InputField):
    css_class = 'input-medium'


class TextField(InputField, twf.TextField):
    pass


class TextArea(BootstrapMixin, twf.TextArea):
    css_class = 'input-xlarge'


class _BoolControl(BootstrapMixin):
    template = "tw2.bootstrap.forms.templates.bool_control"

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


class FileField(BootstrapMixin, twf.FileField):
    css_class = "input-file"


class HiddenField(twf.HiddenField):
    pass


class IgnoredField(twf.HiddenField):
    pass


class LabelField(BootstrapMixin, twf.LabelField):
    template = "tw2.bootstrap.forms.templates.label_field"
    css_class = "input-medium uneditable-input"

    def prepare(self):
        super(LabelField, self).prepare()
        self.safe_modify('attrs')
        del self.attrs['class']


class LinkField(BootstrapMixin, twf.LinkField):
    """ TODO -- not sure how to take this one on.

    It doesn't seem to nicely fit the bootstrap paradigm.  Do you have
    any ideas?
    """
    pass


class Button(BootstrapMixin, twf.Button):
    css_class = 'btn'


class SubmitButton(Button, twf.SubmitButton):
    css_class = 'btn btn-primary'


class ResetButton(Button, twf.ResetButton):
    pass


class HorizontalLayout(BootstrapMixin, twf.widgets.BaseLayout):
    __doc__ = """
    Arrange widgets and labels horizontally:
    Float left, right-aligned labels on same line as controls
    """ + twf.widgets.BaseLayout.__doc__
    template = "mako:tw2.bootstrap.forms.templates.horizontal_layout"


class BootstrapForm(BootstrapMixin, twf.Form):
    """ Base class for bootstrap forms. """
    children = twc.Required
    submit = SubmitButton(id='submit', value='Save')


class HorizontalForm(BootstrapForm):
    """Equivalent to a Form containing a HorizontalLayout."""
    template = "mako:tw2.bootstrap.forms.templates.horizontal_form"
    css_class = "form-horizontal"
    child = twc.Variable(default=HorizontalLayout)

    legend = twc.Param('Legend text for the form.', '')


class CalendarDatePicker(TextField):
    resources = TextField.resources + [datepicker_js, datepicker_css]
    template = "mako:tw2.bootstrap.forms.templates.datepicker"

    style = twc.Param(
        'Specify the template to use. [field, component]',
        default='field')
    format = twc.Param(
        "the date format, combination of d, dd, m, mm, yy, yyyy.",
        default="mm/dd/yyyy")
    date_format = twc.Variable()
    weekStart = twc.Param(
        "day of the week start.  0 for Sunday - 6 for Saturday",
        default=0)
    default = twc.Param(
        'Default value (datetime) for the widget.  If set to a function, ' +
        'it will be called each time before displaying.',
        default=datetime.now)

    def __init__(self, *args, **kw):
        super(CalendarDatePicker, self).__init__(*args, **kw)
        # Convert the bootstrap-datepicker format string to
        # a python format string...
        self.date_format = replace_all(self.format, [
            ('dd', 'DAY'), ('d', 'DAY'),
            ('mm', 'MONTH'), ('m', 'MONTH'),
            ('yyyy', '4YEAR'), ('yy', '2YEAR')
            ])
        self.date_format = replace_all(self.date_format, [
            ('DAY', '%d'),
            ('MONTH', '%m'),
            ('2YEAR', '%y'), ('4YEAR', '%Y')
            ])
        if not self.validator:
            self.validator = twc.DateValidator(
            format=self.date_format,
            )

    def prepare(self):
        super(CalendarDatePicker, self).prepare()
        self.add_call(twj.jQuery(self.selector).datepicker(dict(
            format=self.format,
            weekStart=self.weekStart,
        )))
        if not self.value:
            if callable(self.default):
                self.value = self.default()
            else:
                self.value = self.default
        try:
            self.value = self.value.strftime(self.date_format)
        except:
            pass


class CalendarTimePicker(TextField):
    resources = TextField.resources + [timepicker_js, timepicker_css]

    style = twc.Param(
        'Specify the template to use. [modal, dropdown]',
        default='modal')
    minuteStep = twc.Param(
        'Specify a step for the minute field.',
        default=15)
    defaultTime = twc.Param(
        'Set the initial time value. '
        'Setting it to "current" sets it to the current time.',
        default='current')
    disableFocus = twc.Param(
        'Disables the input from focusing. This is useful for touch screen '
        'devices that display a keyboard on input focus.',
        default=False)

    def prepare(self):
        super(CalendarTimePicker, self).prepare()
        self.add_call(twj.jQuery(self.selector).timepicker(dict(
            template=self.style,
            minuteStep=self.minuteStep,
            defaultTime=self.defaultTime,
            disableFocus=self.disableFocus
        )))


class CalendarDateTimePicker(BootstrapMixin, twc.CompoundWidget):
    resources = set(
        CalendarDatePicker.resources +
        CalendarTimePicker.resources
    )
    date = CalendarDatePicker()
    time = CalendarTimePicker()

    def _validate(self, value, state=None):
        """
        Inner validation method; this is called by validate and should not be
        called directly. Overriding this method in widgets is discouraged; a
        custom validator should be coded instead. However, in some
        circumstances overriding is necessary.
        """
        self._validated = True
        result = ''
        for field in self.children:
            child_value = field.validator.to_python(field.value)
            field.validator.validate_python(child_value, state)
            result += child_value
        return result

    def prepare(self):
        super(CalendarDateTimePicker, self).prepare()


class CheckBoxList(BootstrapMixin, twf.CheckBoxList):
    template = "tw2.bootstrap.forms.templates.selection_list"


class CheckBoxTable(BootstrapMixin, twf.CheckBoxTable):
    template = "tw2.bootstrap.forms.templates.selection_table"


class DataGrid(BootstrapMixin, twf.DataGrid):
    pass


class FieldSet(BootstrapMixin, twf.FieldSet):
    pass


class Form(BootstrapMixin, twf.Form):
    pass


class FormPage(BootstrapMixin, twf.FormPage):
    pass


class GridLayout(BootstrapMixin, twf.GridLayout):
    pass


class ImageButton(BootstrapMixin, twf.ImageButton):
    pass


class Label(BootstrapMixin, twf.Label):
    pass


class ListFieldSet(BootstrapMixin, twf.ListFieldSet):
    pass


class ListForm(BootstrapForm, twf.ListForm):
    pass


class ListLayout(BootstrapMixin, twf.ListLayout):
    pass


class MultipleSelectField(BootstrapMixin, twf.MultipleSelectField):
    pass


class MultipleSelectionField(BootstrapMixin, twf.MultipleSelectionField):
    pass


class PostlabeledCheckBox(BootstrapMixin, twf.PostlabeledCheckBox):
    pass


class PostlabeledPartialRadioButton(BootstrapMixin,
                                    twf.PostlabeledPartialRadioButton):
    pass


class RadioButtonList(BootstrapMixin, twf.RadioButtonList):
    template = "tw2.bootstrap.forms.templates.selection_list"


class RadioButtonTable(BootstrapMixin, twf.RadioButtonTable):
    template = "tw2.bootstrap.forms.templates.selection_table"


class RowLayout(BootstrapMixin, twf.RowLayout):
    pass


class SelectionField(BootstrapMixin, twf.SelectionField):
    pass


class SeparatedCheckBoxTable(BootstrapMixin, twf.SeparatedCheckBoxTable):
    pass


class SeparatedRadioButtonTable(BootstrapMixin, twf.SeparatedRadioButtonTable):
    pass


class SingleSelectField(BootstrapMixin, twf.SingleSelectField):
    pass


class Spacer(BootstrapMixin, twf.Spacer):
    template = "tw2.bootstrap.forms.templates.spacer"


class TableFieldSet(BootstrapMixin, twf.TableFieldSet):
    pass


class TableForm(BootstrapForm, twf.TableForm):
    pass


class TableLayout(BootstrapMixin, twf.TableLayout):
    pass


class VerticalCheckBoxTable(SelectionField, twf.VerticalCheckBoxTable):
    template = "tw2.bootstrap.forms.templates.vertical_selection_table"
    css_class = "table table-condensed"


class VerticalRadioButtonTable(SelectionField, twf.VerticalRadioButtonTable):
    template = "tw2.bootstrap.forms.templates.vertical_selection_table"
    css_class = "table table-condensed"
