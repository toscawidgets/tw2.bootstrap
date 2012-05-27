from tw2.core.testbase import (
    WidgetTest as _WidgetTest,
)
import tw2.core as twc
import tw2.forms as twf
import tw2.bootstrap as twb


def test_every_widget_exposed():
    """ Is widget exposed by tw2.forms also in tw2.bootstrap? """

    is_widget = lambda obj: isinstance(obj, twc.widgets.WidgetMeta)

    twf_widgets = filter(is_widget, [getattr(twf, attr) for attr in dir(twf)])
    twb_widgets = filter(is_widget, [getattr(twb, attr) for attr in dir(twb)])
    twf_widget_names = [w.__name__ for w in twf_widgets]
    twb_widget_names = [w.__name__ for w in twb_widgets]

    def _is_widget_covered(name):
        assert name in twb_widget_names, \
                "%r in tw2.forms but not tw2.bootstrap" % name

    for twf_widget in twf_widgets:
        yield _is_widget_covered, twf_widget.__name__


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
