#!/usr/bin/env python
#-*- coding: utf-8 -*-

from distutils.core import setup

version = __import__('pelican_jsfiddle').__version__

setup(
    name="pelican-jsfiddle",
    version=version,
    url='https://github.com/if1live/pelican-jsfiddle',
    author="libsora",
    author_email="libsora25@gmail.com",
    maintainer="libsora",
    maintainer_email="libsora25@gmail.com",
    description="Easily embed JSFiddle in your articles",
    long_description=open("README.md").read(),
    license="MIT",
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
