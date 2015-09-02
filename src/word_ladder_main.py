"""
Main file for making a ladder between two words.
"""

import sys
import WordGraph


def make_ladder(first, second, debug):
    """Return a WordGraph from the first word to the second word."""

    # There's lots of funny pep8 rules about how many empty lines and such to have. How interesting
    # Also pycharm is kinda sick. You ever used intelliJ for java? It's the same company

    if debug:
        print 'Creating a word graph from "%s" to "%s"' % (first, second)

    graph = WordGraph.WordGraph()

    return graph


if __name__ == '__main__':
    debug = False
    for arg in sys.argv:
        if arg == "-d":
            debug = True

    first = raw_input('First word: ')
    second = raw_input('Second word: ')

    graph = make_ladder(first, second, debug)

    print 'graph:', graph
