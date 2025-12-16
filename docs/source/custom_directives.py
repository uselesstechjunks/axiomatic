from docutils import nodes
from docutils.parsers.rst import Directive

class DefinitionsDirective(Directive):
	has_content = True

def run(self):
	node = nodes.admonition('', nodes.title(text='Definitions'))
	self.state.nested_parse(self.content, self.content_offset, node)
	return [node]
