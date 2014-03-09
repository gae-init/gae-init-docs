# -*- coding: utf-8 -*-
"""
    jinja2_markdown
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A jinja2 extension that adds a `{% markdown %}` tag.

    :copyright: (c) 2014 by Daniel Chatfield
"""

import markdown
from jinja2.nodes import CallBlock
from jinja2.ext import Extension


class MarkdownExtension(Extension):
    tags = set(['markdown'])

    def __init__(self, environment):
        super(MarkdownExtension, self).__init__(environment)
        environment.extend(
            markdowner=markdown.Markdown(extensions=['extra'])
        )

    def parse(self, parser):
        lineno = parser.stream.next().lineno
        body = parser.parse_statements(
            ['name:endmarkdown'],
            drop_needle=True
        )
        return CallBlock(
            self.call_method('_markdown_support'),
            [],
            [],
            body
        ).set_lineno(lineno)

    def _markdown_support(self, caller):
        block = caller()
        block = self._strip_whitespace(block)
        return self._render_markdown(block)

    def _strip_whitespace(self, block):
        lines = block.split('\n')
        whitespace = ''
        output = ''

        if (len(lines) > 1):
            for char in lines[1]:
                if (char == ' ' or char == '\t'):
                    whitespace += char
                else:
                    break

        for line in lines:
            output += line.replace(whitespace, '', 1) + '\r\n'

        return output.strip()

    def _render_markdown(self, block):
        block = self.environment.markdowner.convert(block)
        return '<!-- MARKDOWN -->\n' + block + '\n<!-- ENDMARKDOWN -->'
