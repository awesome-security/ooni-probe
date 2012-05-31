#!/usr/bin/env python

"""
This script should be used for creating the scaffolding for a test.
"""
import os
import sys

test_template = """\"\"\"
This is a self genrated test created by scaffolding.py.
you will need to fill it up with all your necessities.
Safe hacking :).
\"\"\"
from zope.interface import implements
from twisted.python import usage
from twisted.plugin import IPlugin
from plugoo.tests import ITest, TwistedTest

class %(testName)sArgs(usage.Options):
    optParameters = [['asset', 'a', None, 'Asset file'],
                     ['resume', 'r', 0, 'Resume at this index']]

class %(testName)sTest(TwistedTest):
    implements(IPlugin, ITest)

    shortName = "%(testShortname)s"
    description = "%(testName)s"
    requirements = None
    options = %(testName)sArgs
    blocking = True

    def control(self, experiment_result, args):
        # What you return here ends up inside of the report.
        return {}

    def experiment(self, args):
        # What you return here gets handed as input to control
        return {}

    def load_assets(self):
        if self.local_options:
            return {'asset': Asset(self.local_options['asset'])}
        else:
            return {}

# We need to instantiate it otherwise getPlugins does not detect it
# XXX Find a way to load plugins without instantiating them.
%(testShortname)s = %(testName)sTest(None, None, None)
"""

test_vars = {'testName': None, 'testShortname': None}
test_vars['testName'] = raw_input('Test Name: ')
test_vars['testShortname'] = raw_input("Test Short Name: ")

fname = test_vars['testShortname']+'.py'

if os.path.exists(fname):
    print 'WARNING! File named "%s" already exists.' % fname
    if raw_input("Do you wish to continue (y/N)? ").lower() != 'y':
        print "gotcha! Dying.."
        sys.exit(0)

fp = open(fname, 'w')
fp.write(test_template % test_vars)
fp.close()

