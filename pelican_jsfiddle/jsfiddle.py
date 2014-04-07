#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from docutils import nodes
from docutils.parsers.rst import directives, Directive

class JSFiddle(Directive):
    u"""
    Embed JSFiddle in articles.

    Based on the pelican-youtube by Kura
    https://github.com/kura/pelican_youtube

    FIDDLE_ID is required.
    width, height are optional.

    FIDDLE_ID is....
    http://jsfiddle.net/if1live/V2P28/
                        ------------- => if1live/V2P28

    Usage:
    .. jsfiddle:: FIDDLE_ID
        :width: 100%
        :height: 300

    Example:
    .. jsfiddle:: if1live/V2P28
        :width: 100%
        :height: 300
    """
    required_arguments = 1
    optional_arguments = 2
    option_spec = {
        'width': directives.length_or_percentage_or_unitless,
        'height': directives.length_or_percentage_or_unitless,
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):
        fiddle_id = self.arguments[0].strip()
        width = '100%'
        height = '300'

        width = self.options.get('width', '100%')
        height = self.options.get('height', '300')

        url = 'http://jsfiddle.net/{}/embedded/'.format(fiddle_id)
        div_block = '<div class="jsfiddle">'
        embed_block = '<iframe width="{}" height="{}" src="{}" allowfullscreen="allowfullscreen" frameborder="0"></iframe>'.format(width, height, url)

        return [
            nodes.raw('', div_block, format='html'),
            nodes.raw('', embed_block, format='html'),
            nodes.raw('', '</div>', format='html')
        ]


def register():
    directives.register_directive('jsfiddle', JSFiddle)
