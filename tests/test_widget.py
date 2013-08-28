from tw2.core.testbase import (
    WidgetTest as _WidgetTest,
)
import tw2.core as twc
import tw2.forms as twf
import tw2.bootstrap.forms as twb

import datetime
import six
from six.moves import filter


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

        # These are base-classes that ought not to be displayed on their own.
        twb.BootstrapMixin,
        twb.InputField,
        twb.SelectionField,

        # This doesn't fit into bootstrap very well.
        twb.LinkField,

        # These aren't tested in tw2.forms, so we won't waste our time here.
        twb.SeparatedRadioButtonTable,
        twb.SeparatedCheckBoxTable,
        twb.PostlabeledCheckBox,
        twb.PostlabeledPartialRadioButton,
        twb.FieldSet,
        twb.DataGrid,

        # This one is an abandoned child...
        # Not to be confused with MultipleSelectField.
        twb.MultipleSelectionField
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
           id="bootstrap-test"
           value="" />
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


class TestInlineLayout(WidgetTest):
    widget = twb.InlineLayout
    attrs = {
        'id': 'bootstrap-test',
        'children': [
            twb.ResetButton(id='foo'),
        ],
    }

    expected = """
    <span class="">
      <label for="bootstrap-test:foo">Foo</label>
        <input name="bootstrap-test:foo" type="reset" class="btn" id="bootstrap-test:foo"/>
    </span>
    """


class TestInlineForm(WidgetTest):
    widget = twb.InlineForm
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
          class="form-inline">
      <span class="error"></span>

      <span class="">
        <label for="bootstrap-test:foo">Foo</label>
          <input name="bootstrap-test:foo" type="reset" class="btn" id="bootstrap-test:foo"/>
      </span>

      <input type="submit" class="btn btn-primary" value="Save" id="submit"/>
    </form>
    """


class TestCalendarDatePicker(WidgetTest):
    widget = twb.CalendarDatePicker
    id = 'bootstrap-test'
    value = datetime.datetime.now()
    date_format = '%m/%d/%Y'
    format = 'mm/dd/yyyy'
    attrs = dict(id=id, value=value, date_format=date_format)
    expected = """
    <input name="%(id)s" type="text" id="%(id)s"
           class="input-medium" value="%(value)s" data-date="%(value)s"
           data-date-format="%(format)s" />
    """ % dict(id=id, value=value.strftime(date_format), format=format)


class TestCalendarTimePicker(WidgetTest):
    widget = twb.CalendarTimePicker
    expected = """
    <input name="bootstrap-test" type="text" id="bootstrap-test"
           class="input-medium"/>
    """


class TestCalendarDateTimePicker(WidgetTest):
    widget = twb.CalendarDateTimePicker
    id = 'bootstrap-test'
    value = datetime.datetime.now()
    date_format = '%m/%d/%Y %H:%M:%S'
    format = 'mm/dd/yyyy hh:ii:ss'
    attrs = dict(id=id, value=value, date_format=date_format)
    expected = """
    <div id="%(id)s" class="input-append date">
        <input name="%(id)s" type="text" class="input-medium"
            value="%(value)s" data-date="%(value)s" data-date-format="%(format)s" />
        <span class="add-on"><i class="icon-remove"></i></span>
        <span class="add-on"><i class="icon-calendar"></i></span>
    </div>
    """ % dict(id=id, value=value.strftime(date_format), format=format)


class TestCheckBoxList(WidgetTest):
    widget = twb.CheckBoxList
    attrs = {
        'css_class': 'something',
        'options': (('a', '1'), ('b', '2'), ('c', '3')),
        'id': 'something',
    }
    expected = """<ul class="something" id="something">
    <li>
        <label class="checkbox" for="something:0">
        <input type="checkbox" name="something" value="a" id="something:0">
        1</label>
    </li><li>
        <label class="checkbox" for="something:1">
        <input type="checkbox" name="something" value="b" id="something:1">
        2</label>
    </li><li>
        <label class="checkbox" for="something:2">
        <input type="checkbox" name="something" value="c" id="something:2">
        3</label>
    </li>
</ul>
"""


class TestCheckBoxTable(WidgetTest):
    widget = twb.CheckBoxTable
    attrs = {
        'css_class': 'something',
        'options': (('a', '1'), ('b', '2'), ('c', '3')),
        'id': 'something',
    }
    expected = """
<table class="something" id="something">
    <tbody>
    <tr>
        <td>
            <label class="checkbox" for="something:0">
            <input type="checkbox" name="something"
            value="a" id="something:0">
            1</label>
        </td>
    </tr><tr>
        <td>
            <label class="checkbox" for="something:1">
            <input type="checkbox" name="something"
            value="b" id="something:1">
            2</label>
        </td>
    </tr><tr>
        <td>
            <label class="checkbox" for="something:2">
            <input type="checkbox" name="something"
            value="c" id="something:2">
            3</label>
        </td>
    </tr>
    </tbody>
</table>"""


class TestForm(WidgetTest):
    widget = twb.Form
    attrs = {'child': twb.TableLayout(field1=twb.TextField(id='field1')),
        'buttons': [twb.SubmitButton, twb.ResetButton()]}
    expected = """<form enctype="multipart/form-data" method="post">
        <span class="error"></span>
        <table>
            <tr class="odd" id="field1:container">
                <th><label for="field1">Field1</label></th>
                <td >
                <input name="field1" type="text" id="field1" class="input-medium"/>
                    <span id="field1:error"></span>
                </td>
            </tr><tr class="error"><td colspan="2">
                <span id=":error"></span>
            </td></tr>
        </table>
            <input type="submit" class="btn btn-primary"/>
            <input type="reset" class="btn"/>
        </form>"""


class TestFormPage(WidgetTest):
    widget = twb.FormPage
    attrs = {'child': twb.TableForm(children=[
        twb.TextField(id='field1'),
        twb.TextField(id='field2'),
        twb.TextField(id='field3'),
        ]),
        'title': 'some title',
        'id': 'mytestwidget',
    }
    expected = """<html>
<head><title>some title</title></head>
<body id="mytestwidget:page"><h1>some title</h1><form method="post" id="mytestwidget:form" enctype="multipart/form-data">
     <span class="error"></span>
    <table id="mytestwidget">
    <tr class="odd" id="mytestwidget:field1:container">
        <th>Field1</th>
        <td>
            <input name="mytestwidget:field1" id="mytestwidget:field1" type="text" class="input-medium">
            <span id="mytestwidget:field1:error"></span>
        </td>
    </tr><tr class="even" id="mytestwidget:field2:container">
        <th>Field2</th>
        <td>
            <input name="mytestwidget:field2" id="mytestwidget:field2" type="text" class="input-medium">
            <span id="mytestwidget:field2:error"></span>
        </td>
    </tr><tr class="odd" id="mytestwidget:field3:container">
        <th>Field3</th>
        <td>
            <input name="mytestwidget:field3" id="mytestwidget:field3" type="text" class="input-medium">
            <span id="mytestwidget:field3:error"></span>
        </td>
    </tr>
    <tr class="error"><td colspan="2">
        <span id="mytestwidget:error"></span>
    </td></tr>
</table>
    <input type="submit" id="submit" value="Save" class="btn btn-primary"/>
</form></body>
</html>"""


class TestGridLayout(WidgetTest):
    widget = twb.GridLayout
    attrs = {'children': [twb.TextField(id='field1'),
                          twb.TextField(id='field2'),
                          twb.TextField(id='field3')],
             'repetition': 1,
             }
    expected = """
    <table>
    <tr><th>Field1</th><th>Field2</th><th>Field3</th></tr>
    <tr class="error"><td colspan="0" id=":error">
    </td></tr>
    </table>"""


class TestImageButton(WidgetTest):
    widget = twb.ImageButton
    attrs = {
        'value': 'info',
        'name': 'hidden_name',
        'link': '/somewhere.gif',
    }
    expected = """
    <input src="/somewhere.gif" name="hidden_name"
           value="info" alt="" type="image">
    """


class TestLabel(WidgetTest):
    widget = twb.Label
    attrs = {'text': 'something'}
    expected = """<span>something</span>"""


class TestListFieldset(WidgetTest):
    widget = twb.ListFieldSet
    attrs = {'field1': twb.TextField(id='field1'),
             'field2': twb.TextField(id='field2'),
             'field3': twb.TextField(id='field3'),
             }
    expected = """<fieldset >
    <legend></legend>
    <ul >
    <li class="odd">
     <label for="field1">Field1</label>
        <input name="field1" id="field1" type="text" class="input-medium"/>
        <span id="field1:error" class="error"></span>
    </li>
    <li class="even">
     <label for="field2">Field2</label>
        <input name="field2" id="field2" type="text" class="input-medium"/>
        <span id="field2:error" class="error"></span>
    </li>
    <li class="odd">
     <label for="field3">Field3</label>
        <input name="field3" id="field3" type="text" class="input-medium"/>
        <span id="field3:error" class="error"></span>
    </li>
    <li class="error"><span id=":error" class="error"></span></li>
</ul>
</fieldset>"""


class TestListForm(WidgetTest):
    widget = twb.ListForm
    attrs = {'field1': twb.TextField(id='field1'),
             'field2': twb.TextField(id='field2'),
             'field3': twb.TextField(id='field3'),
             }
    expected = """<form method="post" enctype="multipart/form-data">
     <span class="error"></span>
    <ul >
    <li class="odd">
     <label for="field1">Field1</label>
        <input name="field1" id="field1" type="text" class="input-medium"/>
        <span id="field1:error" class="error"></span>
    </li>
    <li class="even">
     <label for="field2">Field2</label>
        <input name="field2" id="field2" type="text" class="input-medium"/>
        <span id="field2:error" class="error"></span>
    </li>
    <li class="odd">
     <label for="field3">Field3</label>
        <input name="field3" id="field3" type="text" class="input-medium"/>
        <span id="field3:error" class="error"></span>
    </li>
    <li class="error"><span id=":error" class="error"></span></li>
</ul>
    <input type="submit" id="submit" value="Save" class="btn btn-primary">
</form>"""


class TestListLayout(WidgetTest):
    widget = twb.ListLayout
    attrs = {'children': [
        twb.TextField(id='field1'),
        twb.TextField(id='field2'),
        twb.TextField(id='field3'),
    ]}
    expected = """\
<ul>
    <li class="odd">
     <label for="field1">Field1</label>
        <input name="field1" id="field1" type="text" class="input-medium">
        <span id="field1:error" class="error"></span>
    </li><li class="even">
     <label for="field2">Field2</label>
        <input name="field2" id="field2" type="text" class="input-medium">
        <span id="field2:error" class="error"></span>
    </li><li class="odd">
     <label for="field3">Field3</label>
        <input name="field3" id="field3" type="text" class="input-medium">
        <span id="field3:error" class="error"></span>
    </li>
    <li class="error"><span id=":error" class="error"></span></li>
</ul>"""
    declarative = True


class TestMultipleSelectField(WidgetTest):
    widget = twb.MultipleSelectField
    attrs = {
        'css_class': 'something',
        'options': (('a', '1'), ('b', '2'), ('c', '3')),
        'id': "hid",
    }
    expected = """
    <select class="something" multiple="multiple" id="hid" name="hid">
                      <option value="a">1</option>
                      <option value="b">2</option>
                      <option value="c">3</option>
                  </select>"""
    validate_params = [[None, {'hid':'b'}, [six.u('b')]]]


class TestRadioButtonList(WidgetTest):
    widget = twb.RadioButtonList
    attrs = {
        'options': (('a', '1'), ('b', '2'), ('c', '3')),
        'id': 'something',
    }
    expected = """<ul id="something">
    <li>
        <label for="something:0" class="radio">
        <input type="radio" name="something" value="a" id="something:0">
        1</label>
    </li><li>
        <label for="something:1" class="radio">
        <input type="radio" name="something" value="b" id="something:1">
        2</label>
    </li><li>
        <label for="something:2" class="radio">
        <input type="radio" name="something" value="c" id="something:2">
        3</label>
    </li>
</ul>"""


class TestRadioButtonTable(WidgetTest):
    widget = twb.RadioButtonTable
    attrs = {
        'options': (('a', '1'), ('b', '2'), ('c', '3')),
        'id': 'something',
    }
    expected = """<table id="something">
    <tbody>
    <tr>
        <td>
            <label for="something:0" class="radio">
            <input type="radio" name="something" value="a" id="something:0">
            1</label>
        </td>
    </tr><tr>
        <td>
            <label for="something:1" class="radio">
            <input type="radio" name="something" value="b" id="something:1">
            2</label>
        </td>
    </tr><tr>
        <td>
            <label for="something:2" class="radio">
            <input type="radio" name="something" value="c" id="something:2">
            3</label>
        </td>
    </tr>
    </tbody>
</table>"""


class TestRowLayout(WidgetTest):
    widget = twb.RowLayout
    attrs = {'children': [twb.TextField(id='field1'),
                          twb.TextField(id='field2'),
                          twb.TextField(id='field3')],
             'repetition': 1,
             }
    expected = """
    <tr class="even">
    <td>
        <input name="field1" id="field1" type="text" class="input-medium">
    </td><td>
        <input name="field2" id="field2" type="text" class="input-medium">
    </td><td>
        <input name="field3" id="field3" type="text" class="input-medium">
    </td>
    <td>
    </td>
    </tr>"""


class TestSingleSelectField(WidgetTest):
    """ There's actually nothing special about this guy.  """
    widget = twb.SingleSelectField
    attrs = {
        'options': ((1, 'a'), (2, 'b'), (3, 'c')),
        'id': 'hid',
        'validator': twc.IntValidator(),
    }
    expected = """<select id="hid" name="hid">
                        <option></option>
                        <option value="1">a</option>
                        <option value="2">b</option>
                        <option value="3">c</option>
                  </select>"""


class TestSpacer(WidgetTest):
    widget = twb.Spacer
    expected = """<hr name="bootstrap-test" id="bootstrap-test"></hr>"""


class TestTableForm(WidgetTest):
    widget = twb.TableForm
    attrs = {'field1': twb.TextField(id='field1'),
             'field2': twb.TextField(id='field2'),
             'field3': twb.TextField(id='field3'),
             }
    expected = """<form method="post" enctype="multipart/form-data">
     <span class="error"></span>
    <table>
    <tr class="odd" id="field1:container">
        <th><label for="field1">Field1</label></th>
        <td>
            <input name="field1" id="field1" type="text" class="input-medium">
            <span id="field1:error"></span>
        </td>
    </tr><tr class="even" id="field2:container">
        <th><label for="field2">Field2</label></th>
        <td>
            <input name="field2" id="field2" type="text" class="input-medium">
            <span id="field2:error"></span>
        </td>
    </tr><tr class="odd" id="field3:container">
        <th><label for="field3">Field3</label></th>
        <td>
            <input name="field3" id="field3" type="text" class="input-medium">
            <span id="field3:error"></span>
        </td>
    </tr>
    <tr class="error"><td colspan="2">
        <span id=":error"></span>
    </td></tr>
</table>
    <input type="submit" id="submit" value="Save" class="btn btn-primary">
</form>"""


class TestTableFieldset(WidgetTest):
    widget = twb.TableFieldSet
    attrs = {'field1': twb.TextField(id='field1'),
             'field2': twb.TextField(id='field2'),
             'field3': twb.TextField(id='field3'),
             }
    expected = """<fieldset>
    <legend></legend>
    <table>
    <tr class="odd" id="field1:container">
        <th><label for="field1">Field1</label></th>
        <td>
            <input name="field1" id="field1" type="text" class="input-medium">
            <span id="field1:error"></span>
        </td>
    </tr><tr class="even" id="field2:container">
        <th><label for="field2">Field2</label></th>
        <td>
            <input name="field2" id="field2" type="text" class="input-medium">
            <span id="field2:error"></span>
        </td>
    </tr><tr class="odd" id="field3:container">
        <th><label for="field3">Field3</label></th>
        <td>
            <input name="field3" id="field3" type="text" class="input-medium">
            <span id="field3:error"></span>
        </td>
    </tr>
    <tr class="error"><td colspan="2">
        <span id=":error"></span>
    </td></tr>
</table>
</fieldset>"""


class TestTableLayout(WidgetTest):
    widget = twb.TableLayout
    attrs = {'children': [twb.TextField(id='field1'),
                          twb.TextField(id='field2'),
                          twb.TextField(id='field3')]}
    expected = """<table>
    <tr class="odd" id="field1:container">
        <th><label for="field1">Field1</label></th>
        <td>
            <input name="field1" id="field1" type="text" class="input-medium">
            <span id="field1:error"></span>
        </td>
    </tr><tr class="even" id="field2:container">
        <th><label for="field2">Field2</label></th>
        <td>
            <input name="field2" id="field2" type="text" class="input-medium">
            <span id="field2:error"></span>
        </td>
    </tr><tr class="odd" id="field3:container">
        <th><label for="field3">Field3</label></th>
        <td>
            <input name="field3" id="field3" type="text" class="input-medium">
            <span id="field3:error"></span>
        </td>
    </tr>
    <tr class="error"><td colspan="2">
        <span id=":error"></span>
    </td></tr>
</table>"""


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
