#!/usr/bin/env python
#-*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
import re
import os

# https://github.com/zzzeek/sqlalchemy/blob/master/setup.py
v_file = open(os.path.join(os.path.dirname(__file__), 'pelican_jsfiddle', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)
v_file.close()

download_url = 'https://github.com/if1live/pelican-jsfiddle/tarball/{}'.format(VERSION)

packages = [
    'pelican_jsfiddle',
]

requires = [
    'docutils>=0.11',
]

tests_require = [
    'nose',
]

setup(
    name="pelican-jsfiddle",
    version=VERSION,
    url='https://github.com/if1live/pelican-jsfiddle',
    download_url=download_url,
    author="libsora",
    author_email="libsora25@gmail.com",
    maintainer="libsora",
    maintainer_email="libsora25@gmail.com",
    description="Easily embed JSFiddle in your articles",
    long_description=open("README.rst").read(),
    license="MIT",
    packages=packages,
    package_data={'': ['LICENSE', ]},
    include_package_data=True,
    install_requires=requires,
    tests_require=tests_require,
    keywords=['pelican', 'jsfiddle', 'plugin'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ],
)
