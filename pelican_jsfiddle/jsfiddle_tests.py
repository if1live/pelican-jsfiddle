#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import docutils.core
from pelican_jsfiddle import register as register_jsfiddle
from pelican_jsfiddle import jsfiddle


class comma_seperated_multiple_choices_Test(unittest.TestCase):
    def test_error(self):
        multiple_choices = jsfiddle.comma_seperated_multiple_choices
        keylist = ('js', 'resources', 'html', 'css', 'result')

        argument = 'not-exist'
        self.assertRaises(ValueError, multiple_choices, argument, keylist)

        argument = 'js,not-exist'
        self.assertRaises(ValueError, multiple_choices, argument, keylist)

    def test_ok(self):
        # single
        multiple_choices = jsfiddle.comma_seperated_multiple_choices
        keylist = ('js', 'resources', 'html', 'css', 'result')

        argument = 'js'
        self.assertEqual('js', multiple_choices(argument, keylist))

        # many
        argument = 'js,css'
        self.assertEqual('js,css', multiple_choices(argument, keylist))

        # mix whitespace
        argument = '  js, css    ,result  '
        self.assertEqual('js,css,result', multiple_choices(argument, keylist))


class RstTest(unittest.TestCase):
    def test_run(self):
        rest_text = '''
        .. jsfiddle:: if1live/V2P28

        .. jsfiddle:: if1live/V2P28
            :width: 100%
            :height: 150
            :tabs: result,js
            :skin: presentation
        '''

        register_jsfiddle()
        html = docutils.core.publish_string(source=rest_text)
        self.assertNotIn('Error', html)

    def test_error(self):
        rest_text = '''
        .. jsfiddle:: if1live/V2P28
            :tabs: not-valid-tab
        '''
        register_jsfiddle()
        html = docutils.core.publish_string(source=rest_text)
        self.assertIn('Error', html)
