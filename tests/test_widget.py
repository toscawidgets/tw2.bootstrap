from tw2.core.testbase import WidgetTest
from tw2.bootstrap import *

class TestBootstrap(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Bootstrap
    # Initilization args. go here 
    attrs = {'id':'bootstrap-test'}
    params = {}
    expected = """<div id="bootstrap-test"></div>"""
