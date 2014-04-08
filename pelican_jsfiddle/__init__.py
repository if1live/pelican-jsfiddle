# -*- coding: utf-8 -*-

__title__ = 'pelican-jsfiddle'
__version__ = '0.1.0'
__author__ = 'libsora'
__credits__ = ["libsora", ]
__maintainer__ = "libsora"
__email__ = "libsora25@gmail.com"
__status__ = "Beta"
__license__ = 'MIT'
__copyright__ = 'Copyright 2013'

from pelican_jsfiddle.jsfiddle import register

# fix pylint
_register = register
