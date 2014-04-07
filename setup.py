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

packages = [
    'pelican_jsfiddle',
]

requires = [
    'docutils>=0.11',
]

setup(
    name="pelican-jsfiddle",
    version=VERSION,
    url='https://github.com/if1live/pelican-jsfiddle',
    author="libsora",
    author_email="libsora25@gmail.com",
    maintainer="libsora",
    maintainer_email="libsora25@gmail.com",
    description="Easily embed JSFiddle in your articles",
    long_description=open("README.md").read(),
    license="MIT",
    platforms=['linux'],
    packages=find_packages(exclude=["*.tests"]),
    package_data={'': ['LICENSE', ]},
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
