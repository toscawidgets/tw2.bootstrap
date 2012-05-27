"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

from tw2.forms.samples import DemoChildren

from widgets import *


class DemoHorizontalForm(HorizontalForm, DemoChildren):
    legend = 'Hi, I\'m form!'
    buttons = [SubmitButton(), ResetButton()]


class DemoButton(Button):
    pass


class DemoSubmitButton(SubmitButton):
    pass
