"""
Main file for making a ladder between two words.
"""


import time
import sys

from WordGraph import WordGraph


def make_ladder(first, second, debug):
    """Return a WordGraph from the first word to the second word."""
    if debug:
        print '*** Creating a word graph from "%s" to "%s"' % (first, second)

    start_time = time.time()
    graph = WordGraph()
    end_time = time.time()

    if debug:
      print '*** Elapsed time: %f s' % (end_time - start_time)

    return graph


def main():
    debug = False
    for arg in sys.argv:
        if arg == "-d":
            debug = True

    first = raw_input('First word: ')
    second = raw_input('Second word: ')

    graph = make_ladder(first, second, debug)

    print 'graph:', graph


if __name__ == '__main__':
    main()
