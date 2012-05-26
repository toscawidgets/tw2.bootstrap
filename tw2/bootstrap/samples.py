"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import tw2.core as twc
import tw2.forms as twf
import widgets



class DemoChildren(twc.CompoundWidget):
    title = twf.TextField()
    priority = twf.SingleSelectField(options=['', 'Normal', 'High'])
    description = twf.TextArea()

class DemoBootstrapHorizontalForm(widgets.BootstrapHorizontalForm, DemoChildren):
    legend = 'Hi, I\'m form!'
    buttons = [twf.SubmitButton(), twf.ResetButton()]

class DemoBootstrapButton(widgets.BootstrapButton):
    pass

class DemoBootstrapSubmitButton(widgets.BootstrapSubmitButton):
    pass
