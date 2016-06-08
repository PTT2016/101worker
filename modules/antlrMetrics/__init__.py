import os
import json
from antlr4 import *
from MyGrammarLexar import MyGrammarLexar
from MyGrammarParser import MyGrammarParser

def main(argv):
	input=FileStream(argv[1])
	lexer=MyGrammerLexer(input)
	stream = CommonTokenStream(lexer)
	parser = MyGrammarParser(stream)
	tree = paser.StartRule()

if __name__ == '__main__':
	main(sys.argv)


config = {
    'wantdiff': True,
    'wantsfiles': True,
    'threadsafe': True,
    'behavior': {
        'creates': [['resource', 'metric']]
    }
}

# this is the actual logic of the module
def antlr_metrics(source):
    #dummydaten
    nonterminals=0
    references=0
    return [nonterminals,references]

def update_file(context, f):
    # reads the content of the file (primary resource)
    try:
        source = context.get_primary_resource(f)

        metric = antlr_metrics(source)

        context.write_derived_resource(f, metric, 'metric')
    except UnicodeDecodeError:
        context.write_derived_resource(f, [0,0], 'metric')

def remove_file(context, f):
    context.remove_derived_resource(f, 'metric')

def run(context, change):
    # dispatch the modified file
    if change['type'] == 'NEW_FILE':
        update_file(context, change['file'])

    elif change['type'] == 'FILE_CHANGED':
        update_file(context, change['file'])

    else:
        remove_file(context, change['file'])

import unittest
from unittest.mock import Mock
import io
""" bsp tests von simpleLOC
class SimpleLocTest(unittest.TestCase):

    def setUp(self):
        self.env = Mock()
        self.env.get_primary_resource.return_value = 'x = 5\ny=6\nprint(x)\n'

    def test_run_new(self):
        change = {
            'type': 'NEW_FILE',
            'file': 'some-file.py'
        }
        run(self.env, change)

        self.env.write_derived_resource.assert_called_with('some-file.py', 4, 'loc')

    def test_run_changed(self):
        change = {
            'type': 'FILE_CHANGED',
            'file': 'some-file.py'
        }
        run(self.env, change)

        self.env.write_derived_resource.assert_called_with('some-file.py', 4, 'loc')

    def test_run_removed(self):
        change = {
            'type': '',
            'file': 'some-file.py'
        }
        run(self.env, change)

        self.env.remove_derived_resource.assert_called_with('some-file.py', 'loc')

    def test_count_lines_three(self):
        three_lines = '''
        Test
        '''

        self.assertEqual(count_lines(three_lines), 3)

    def test_count_one_line(self):
        one_line = ''

        self.assertEqual(count_lines(one_line), 1)

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleLocTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
"""
