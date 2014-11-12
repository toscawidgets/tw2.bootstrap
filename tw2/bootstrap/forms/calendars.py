'''
Created on 29.05.2012

@author: moschlar
'''
from datetime import datetime

import tw2.core as twc
import tw2.forms as twf
import tw2.jquery as twj

from .widgets import bootstrap_css, bootstrap_js, TextField

# For better calendar widget detection in sprox
try:
    from tw2.forms import CalendarBase
except ImportError:
    CalendarBase = object

__all__ = [
    'CalendarDatePicker',
    'CalendarTimePicker',
    'CalendarDateTimePicker',
]


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

datetimepicker_css = twc.CSSLink(
    modname=__name__,
    filename='static/bootstrap-datetimepicker.css',
    resources=[bootstrap_css])
datetimepicker_js = twc.JSLink(
    modname=__name__,
    filename='static/bootstrap-datetimepicker.js',
    resources=[bootstrap_js],
    location='headbottom')
datetimepicker_resources = [datetimepicker_css, datetimepicker_js]


def replace_all(text, items):
    '''Replaces all old, new tuples from items in text

    items may be a dict of {old: new} pairs
    or a list of (old, new) tuples
    '''
    try:
        items = items.iteritems()
    except:
        pass
    for old, new in items:
        text = text.replace(old, new)
    return text


class _DateFmtConverter(object):
    '''Converter for different date format string syntaxes

    Uses an unambigiuous internal syntax as an intermediate conversion
    step.
    '''
    # TODO: Regexp this?
    js2int = [
        ('dd', 'DAY'), ('d', 'DAY'),
        ('mm', 'MONTH'), ('m', 'MONTH'),
        ('yy', '2YEAR'), ('yyyy', '4YEAR'),
        ('hh', '24HOUR'), ('h', '24HOUR'), ('HH', '12HOUR'), ('H', '12HOUR'),
        ('ii', 'MINUTE'), ('i', 'MINUTE'),
        ('ss', 'SECOND'), ('s', 'SECOND'),
        ('P', 'MERIDIAN'), ('p', 'meridian'),
    ]
    int2js = [(y, x) for (x, y) in js2int]
    py2int = [
        ('%T', '24HOUR:MINUTE:SECOND'), ('%R', '24HOUR:MINUTE'),
        ('%r', '12HOUR:MINUTE:SECOND MERIDIAN'),
        ('%p', 'MERIDIAN'), ('%P', 'meridian'),
        ('%d', 'DAY'),
        ('%m', 'MONTH'),
        ('%Y', '4YEAR'), ('%y', '2YEAR'),
        ('%H', '24HOUR'), ('%I', '12HOUR'),
        ('%M', 'MINUTE'),
        ('%S', 'SECOND'),
        #('%a', ''), ('%A', ''),
        #('%b', ''), ('%B', ''),
    ]
    int2py = [(y, x) for (x, y) in py2int]

    def js2py(self, js):
        _int = replace_all(js, self.js2int)
        py = replace_all(_int, self.int2py)
        return py

    def py2js(self, py):
        _int = replace_all(py, self.py2int)
        js = replace_all(_int, self.int2js)
        return js

datefmtconverter = _DateFmtConverter()


class CalendarDatePicker(TextField, CalendarBase):
    resources = TextField.resources + [datepicker_js, datepicker_css]
    template = "mako:tw2.bootstrap.forms.templates.datepicker"

    style = twc.Param(
        'Specify the template to use. [field, component]',
        default='field')
    date_format = twc.Param(default="%Y-%m-%d")
    format = twc.Variable()
    weekStart = twc.Param(
        "day of the week start.  0 for Sunday - 6 for Saturday",
        default=0)
    default = twc.Param(
        'Default value (datetime) for the widget.  If set to a function, ' +
        'it will be called each time before displaying.',
        default=datetime.now)

    def __init__(self, *args, **kw):
        super(CalendarDatePicker, self).__init__(*args, **kw)
        self.format = datefmtconverter.py2js(self.date_format)
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
        if not self.value and self.required:
            if callable(self.default):
                self.value = self.default()
            else:
                self.value = self.default
        try:
            self.value = self.value.strftime(self.date_format)
        except:
            pass


class CalendarTimePicker(TextField, CalendarBase):
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


class CalendarDateTimePicker(TextField, CalendarBase):

    template = "tw2.bootstrap.forms.templates.datetimepicker"

    resources = TextField.resources + datetimepicker_resources

    date_format = twc.Param(default="%Y-%m-%d %H:%M")
    format = twc.Variable()

    language = twc.Param(default=None)

    datetimepicker_args = twc.Param(default=dict())

    default = twc.Param(
        'Default value (datetime) for the widget.  If set to a function, ' +
        'it will be called each time before displaying.',
        default=datetime.now)

    def __init__(self, *args, **kw):
        super(CalendarDateTimePicker, self).__init__(*args, **kw)
        self.format = datefmtconverter.py2js(self.date_format)
        if 'p' in self.format or 'P' in self.format:
            self.datetimepicker_args.setdefault('showMeridian', True)
        if not self.validator:
            self.validator = twc.DateTimeValidator(
                format=self.date_format,
                required=self.required,
            )

    def prepare(self):
        super(CalendarDateTimePicker, self).prepare()
        self.add_call(twj.jQuery(self.selector).datetimepicker(dict(
            format=self.format,
            language=self.language,
            **self.datetimepicker_args
        )))
        if not self.value and self.required:
            if callable(self.default):
                self.value = self.default()
            else:
                self.value = self.default
        try:
            self.value = unicode(self.value.strftime(self.date_format))
        except:
            pass
