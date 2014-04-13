# pelican-jsfiddle

[![Build Status](https://travis-ci.org/if1live/pelican-jsfiddle.svg)](https://travis-ci.org/if1live/pelican-jsfiddle)
[![Coverage Status](https://coveralls.io/repos/if1live/pelican-jsfiddle/badge.png)](https://coveralls.io/r/if1live/pelican-jsfiddle)
[![Requirements Status](https://requires.io/github/if1live/pelican-jsfiddle/requirements.png?branch=master)](https://requires.io/github/if1live/pelican-jsfiddle/requirements/?branch=master)
[![Code Health](https://landscape.io/github/if1live/pelican-jsfiddle/master/landscape.png)](https://landscape.io/github/if1live/pelican-jsfiddle/master)

Easily embed JSFiddle in your Pelican articles.

## Installation

To install pelican-jsfiddle, simply install it from PyPI:

```bash
$ pip install pelican-jsfiddle
```

Then enabled it in your pelicanconf.py

```python
PLUGINS = [
    # ...
    'pelican_jsfiddle',
    # ...
]
```

## Usage

In your article or page, you simply need to add a line to embed your JSFiddle.

```rst
.. jsfiddle:: FIDDLE_ID
```

Which will result in:

```html
<div class="jsfiddle">
<iframe allowfullscreen="allowfullscreen" frameborder="0" height="300" src="http://jsfiddle.net/<FIDDLE_ID>/embedded/js,resources,html,css,result/light/" width="100%">
</iframe>
</div>
```

### Additional arguments

You can also specify a ```width```, ```height```, ```tabs``` and ```skin```

```rst
.. jsfiddle:: if1live/V2P28
    :width: 100%
    :height: 300
    :tabs: js,resources,html,css,result
    :skin: light
```


Which will result in:

```html
<div class="jsfiddle">
<iframe allowfullscreen="allowfullscreen" frameborder="0" height="300" src="http://jsfiddle.net/if1live/V2P28/embedded/js,resources,html,css,result/light/" width="100%">
</iframe>
</div>
```
