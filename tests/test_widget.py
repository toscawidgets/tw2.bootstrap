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

    def _is_widget_exposed(name):
        msg = "%r in tw2.forms but not tw2.bootstrap" % name
        assert name in twb_widget_names, msg

    for twf_widget in twf_widgets:
        yield _is_widget_exposed, twf_widget.__name__


def test_every_widget_covered():
    """ Is there a test for tw2.bootstrap widget's output? """

    # Check that there is a test for every widget except the following.
    # They are excluded for various reasons, mostly because they cannot be
    # rendered on their own.
    excluded = [
        twb.bootstrap_css,
        twb.bootstrap_responsive_css,
        twb.bootstrap_js,

        twb.Bootstrap,
        twb.InputField,
        twb.LinkField,
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


class WidgetTest(_WidgetTest):
    """ Only test against mako (we don't provide other templates). """
    engines = ['mako']

    # Universal initilization args. go here
    attrs = {'id': 'bootstrap-test'}
    params = {}


class TestTextField(WidgetTest):
    widget = twb.TextField
    expected = """
    <input name="bootstrap-test"
           id="bootstrap-test"
           class="input-medium"
           type="text">
    </input>
    """


class TestTextArea(WidgetTest):
    widget = twb.TextArea
    expected = """
    <textarea name="bootstrap-test"
              id="bootstrap-test"
              class="input-xlarge">
    </textarea>
    """


class TestCheckBox(WidgetTest):
    widget = twb.CheckBox
    expected = """
    <label class="checkbox">
        <input name="bootstrap-test" type="checkbox"
               id="bootstrap-test"/>
    </label>
    """


class TestRadioButton(WidgetTest):
    widget = twb.RadioButton
    expected = """
    <label class="radio">
        <input name="bootstrap-test" type="radio"
               id="bootstrap-test"/>
    </label>
    """


class TestPasswordField(WidgetTest):
    widget = twb.PasswordField
    expected = """
    <input name="bootstrap-test" type="password"
           class="input-medium" id="bootstrap-test"/>
    """


class TestFileField(WidgetTest):
    widget = twb.FileField
    expected = """
    <input name="bootstrap-test"
           type="file"
           class="input-file"
           id="bootstrap-test"/>
   """


class TestHiddenField(WidgetTest):
    widget = twb.HiddenField
    expected = """
    <input type="hidden" name="bootstrap-test" id="bootstrap-test"/>
    """


class TestIgnoredField(WidgetTest):
    widget = twb.IgnoredField
    expected = """
    <input type="hidden" name="bootstrap-test" id="bootstrap-test"/>
    """


class TestLabelField(WidgetTest):
    widget = twb.LabelField
    attrs = dict(id="bootstrap-test", value="foo")
    expected = """
    <span class="input-medium uneditable-input">foo<input
       type="hidden" id="bootstrap-test"
       value="foo" name="bootstrap-test"/>
    </span>
    """


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


class TestHorizontalLayout(WidgetTest):
    widget = twb.HorizontalLayout
    attrs = {
        'id': 'bootstrap-test',
        'children': [
            twb.ResetButton(id='foo'),
        ],
    }

    expected = """
    <div class="control-group ">
      <label class="control-label" for="bootstrap-test:foo">Foo</label>
      <div class="controls">
        <input id="bootstrap-test:foo"
               name="bootstrap-test:foo"
               type="reset"
               class="btn"/>
      </div>
    </div>
    """


class TestHorizontalForm(WidgetTest):
    widget = twb.HorizontalForm
    attrs = {
        'id': 'bootstrap-test',
        'children': [
            twb.ResetButton(id='foo'),
        ],
    }

    expected = """
    <form id="bootstrap-test:form"
          enctype="multipart/form-data"
          method="post"
          class="form-horizontal">
         <span class="error"></span>

      <fieldset>

        <div class="control-group ">
          <label class="control-label" for="bootstrap-test:foo">Foo</label>
          <div class="controls">
            <input type="reset" class="btn"
                   id="bootstrap-test:foo"
                   name="bootstrap-test:foo"/>
          </div>
        </div>

        <div class="form-actions">
          <input type="submit" class="btn btn-primary"
                 value="Save" id="submit"/>
        </div>
      </fieldset>
    </form>
    """


class TestCalendarDatePicker(WidgetTest):
    widget = twb.CalendarDatePicker
    expected = """
    <input name="bootstrap-test" type="text" id="bootstrap-test"
           class="input-medium"/>
    """


class TestCalendarTimePicker(WidgetTest):
    widget = twb.CalendarTimePicker
    expected = """<TODO>How should this actually work?</TODO>"""


class TestCalendarDateTimePicker(WidgetTest):
    widget = twb.CalendarDateTimePicker
    expected = """<TODO>How should this actually work?</TODO>"""


class TestCheckBoxList(WidgetTest):
    widget = twb.CheckBoxList
    expected = """<TODO>How should this actually work?</TODO>"""


class TestCheckBoxTable(WidgetTest):
    widget = twb.CheckBoxTable
    expected = """<TODO>How should this actually work?</TODO>"""


class TestDataGrid(WidgetTest):
    widget = twb.DataGrid
    expected = """<TODO>How should this actually work?</TODO>"""


class TestFieldSet(WidgetTest):
    widget = twb.FieldSet
    expected = """<TODO>How should this actually work?</TODO>"""


class TestForm(WidgetTest):
    widget = twb.Form
    expected = """<TODO>How should this actually work?</TODO>"""


class TestFormPage(WidgetTest):
    widget = twb.FormPage
    expected = """<TODO>How should this actually work?</TODO>"""


class TestGridLayout(WidgetTest):
    widget = twb.GridLayout
    expected = """<TODO>How should this actually work?</TODO>"""


class TestImageButton(WidgetTest):
    widget = twb.ImageButton
    expected = """<TODO>How should this actually work?</TODO>"""


class TestLabel(WidgetTest):
    widget = twb.Label
    expected = """<TODO>How should this actually work?</TODO>"""


class TestListFieldSet(WidgetTest):
    widget = twb.ListFieldSet
    expected = """<TODO>How should this actually work?</TODO>"""


class TestListForm(WidgetTest):
    widget = twb.ListForm
    expected = """<TODO>How should this actually work?</TODO>"""


class TestListLayout(WidgetTest):
    widget = twb.ListLayout
    expected = """<TODO>How should this actually work?</TODO>"""


class TestMultipleSelectField(WidgetTest):
    widget = twb.MultipleSelectField
    expected = """<TODO>How should this actually work?</TODO>"""


class TestMultipleSelectionField(WidgetTest):
    widget = twb.MultipleSelectionField
    expected = """<TODO>How should this actually work?</TODO>"""


class TestPostlabeledCheckBox(WidgetTest):
    widget = twb.PostlabeledCheckBox
    expected = """<TODO>How should this actually work?</TODO>"""


class TestPostlabeledPartialRadioButton(WidgetTest):
    widget = twb.PostlabeledPartialRadioButton
    expected = """<TODO>How should this actually work?</TODO>"""


class TestRadioButtonList(WidgetTest):
    widget = twb.RadioButtonList
    expected = """<TODO>How should this actually work?</TODO>"""


class TestRadioButtonTable(WidgetTest):
    widget = twb.RadioButtonTable
    expected = """<TODO>How should this actually work?</TODO>"""


class TestRowLayout(WidgetTest):
    widget = twb.RowLayout
    expected = """<TODO>How should this actually work?</TODO>"""


class TestSelectionField(WidgetTest):
    widget = twb.SelectionField
    expected = """<TODO>How should this actually work?</TODO>"""


class TestSeparatedCheckBoxTable(WidgetTest):
    widget = twb.SeparatedCheckBoxTable
    expected = """<TODO>How should this actually work?</TODO>"""


class TestSeparatedRadioButtonTable(WidgetTest):
    widget = twb.SeparatedRadioButtonTable
    expected = """<TODO>How should this actually work?</TODO>"""


class TestSingleSelectField(WidgetTest):
    widget = twb.SingleSelectField
    expected = """<TODO>How should this actually work?</TODO>"""


class TestSpacer(WidgetTest):
    widget = twb.Spacer
    expected = """<hr name="bootstrap-test" id="bootstrap-test"></hr>"""


class TestTableForm(WidgetTest):
    widget = twb.TableForm
    expected = """<TODO>How should this actually work?</TODO>"""


class TestTableFieldSet(WidgetTest):
    widget = twb.TableFieldSet
    expected = """<TODO>How should this actually work?</TODO>"""


class TestTableLayout(WidgetTest):
    widget = twb.TableLayout
    expected = """<TODO>How should this actually work?</TODO>"""


class TestVerticalCheckBoxTable(WidgetTest):
    widget = twb.VerticalCheckBoxTable
    attrs = dict(id='bootstrap-test', options=['', 'Red', 'Blue'])
    expected = """
    <table class="table table-condensed"
           name="bootstrap-test"
           id="bootstrap-test">
        <tbody>
        <tr><td/></tr>
        <tr>
            <td>
              <label class="checkbox" for="bootstrap-test:1">
                <input type="checkbox" name="bootstrap-test"
                       value="Red" id="bootstrap-test:1" />Red</label>
            </td>
        </tr>
        <tr>
            <td>
              <label class="checkbox" for="bootstrap-test:2">
                <input type="checkbox" name="bootstrap-test"
                       value="Blue" id="bootstrap-test:2" />Blue</label>
            </td>
        </tr>
        </tbody>
    </table>
    """


class TestVerticalRadioButtonTable(WidgetTest):
    widget = twb.VerticalRadioButtonTable
    attrs = dict(id='bootstrap-test', options=['', 'Red', 'Blue'])
    expected = """
    <table class="table table-condensed"
           name="bootstrap-test"
           id="bootstrap-test">
        <tbody>
        <tr><td/></tr>
        <tr>
            <td>
              <label class="radio" for="bootstrap-test:1">
                <input type="radio" name="bootstrap-test"
                       value="Red" id="bootstrap-test:1" />Red</label>
            </td>
        </tr>
        <tr>
            <td>
              <label class="radio" for="bootstrap-test:2">
                <input type="radio" name="bootstrap-test"
                       value="Blue" id="bootstrap-test:2" />Blue</label>
            </td>
        </tr>
        </tbody>
    </table>
    """
