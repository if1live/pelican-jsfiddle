================
pelican-jsfiddle
================

.. image:: https://travis-ci.org/if1live/pelican-jsfiddle.svg?branch=master
    :target: https://travis-ci.org/if1live/pelican-jsfiddle
.. image:: https://coveralls.io/repos/if1live/pelican-jsfiddle/badge.png
    :target: https://coveralls.io/r/if1live/pelican-jsfiddle
.. image:: https://requires.io/github/if1live/pelican-jsfiddle/requirements.png?branch=master
    :target: https://requires.io/github/if1live/pelican-jsfiddle/requirements/?branch=master
.. image:: https://landscape.io/github/if1live/pelican-jsfiddle/master/landscape.png
    :target: https://landscape.io/github/if1live/pelican-jsfiddle/master

Easily embed JSFiddle in your Pelican articles.

Installation
============

To install pelican-jsfiddle, simply install it from PyPI:

.. code-block:: bash

    $ pip install pelican-jsfiddle


Then enabled it in your pelicanconf.py

.. code-block:: python

    PLUGINS = [
        # ...
        'pelican_jsfiddle',
        # ...
    ]

Usage
=====

In your article or page, you simply need to add a line to embed your JSFiddle.

.. code-block:: rst

    .. jsfiddle:: FIDDLE_ID

Which will result in:

.. code-block:: html

    <div class="jsfiddle">
    <iframe allowfullscreen="allowfullscreen" frameborder="0" height="300" src="http://jsfiddle.net/<FIDDLE_ID>/embedded/js,resources,html,css,result/light/" width="100%">
    </iframe>
    </div>

Additional arguments
----------------------

You can also specify a width, height, tabs and skin.

.. code-block:: rst

    .. jsfiddle:: if1live/V2P28
        :width: 100%
        :height: 300
        :tabs: js,resources,html,css,result
        :skin: light


Which will result in:

.. code-block:: html

    <div class="jsfiddle">
    <iframe allowfullscreen="allowfullscreen" frameborder="0" height="300" src="http://jsfiddle.net/if1live/V2P28/embedded/js,resources,html,css,result/light/" width="100%">
    </iframe>
    </div>


