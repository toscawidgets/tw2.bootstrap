from tw2.core.testbase import (
    WidgetTest as _WidgetTest,
)
import tw2.core as twc
import tw2.forms as twf
import tw2.bootstrap as twb


class WidgetTest(_WidgetTest):
    """ Only test against mako (we don't provide other templates). """
    engines = ['mako']

    # Universal initilization args. go here
    attrs = {'id': 'bootstrap-test'}
    params = {}


class TestButton(WidgetTest):
    widget = twb.Button
    expected = """
    <input  class="btn"
            type="button"
            id="bootstrap-test"
            name="bootstrap-test" />
    """


class TestSubmitButton(WidgetTest):
    widget = twb.SubmitButton
    expected = """
    <input  class="btn btn-primary"
            type="submit"
            id="bootstrap-test" />
    """


class TestResetButton(WidgetTest):
    widget = twb.ResetButton
    expected = """
    <input  class="btn"
            type="reset"
            id="bootstrap-test"
            name="bootstrap-test" />
    """


def test_every_widget_exposed():
    """ Is widget exposed by tw2.forms also in tw2.bootstrap? """

    is_widget = lambda obj: isinstance(obj, twc.widgets.WidgetMeta)

    twf_widgets = filter(is_widget, [getattr(twf, attr) for attr in dir(twf)])
    twb_widgets = filter(is_widget, [getattr(twb, attr) for attr in dir(twb)])
    twf_widget_names = [w.__name__ for w in twf_widgets]
    twb_widget_names = [w.__name__ for w in twb_widgets]

    def _is_widget_exposed(name):
        msg = "%r in tw2.forms but not tw2.bootstrap" % name
        assert name in twb_widget_names, msg

    for twf_widget in twf_widgets:
        yield _is_widget_exposed, twf_widget.__name__


def test_every_widget_covered():
    """ Is there a test for tw2.bootstrap widget's output? """

    # Check that there is a test for every widget except the following
    excluded = [
        twb.Bootstrap,
    ]

    is_widget = lambda obj: isinstance(obj, twc.widgets.WidgetMeta)
    is_test = lambda obj: isinstance(obj, type) and issubclass(obj, WidgetTest)

    twb_widgets = filter(is_widget, [getattr(twb, attr) for attr in dir(twb)])
    twb_widgets = filter(lambda w: w not in excluded, twb_widgets)
    twb_tests = filter(is_test, globals().values())
    tested_widgets = [test.widget for test in twb_tests]

    def _is_widget_covered(widget):
        msg = "tw2.bootstrap.%s is not tested explicitly." % widget.__name__
        assert widget in tested_widgets, msg

    for widget in twb_widgets:
        yield _is_widget_covered, widget
