#!/usr/bin/env python
#-*- coding: utf-8 -*-

import docutils.core
from pelican_jsfiddle import register as register_jsfiddle

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
print html
