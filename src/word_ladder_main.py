"""
Main file for making a ladder between two words.
"""

import time
import sys

from WordGraph import WordGraph


def debug_print(fmt, stuff, debug):
    if debug:
        print '***',
        print fmt % stuff


def make_ladder(first, second, word_file, debug):
    """Return a path from the first word to the second word."""
    debug_print('Creating a word graph from "%s" to "%s"',
                (first, second), debug)

    start_time = time.time()
    graph = make_graph_from_dictionary(word_file, len(first), debug)

    valid = True
    if first not in graph:
        print "Your first word ('%s') is not in the dictionary" % (first)
        valid = False
    if second not in graph:
        print "Your second word ('%s') is not in the dictionary" % (second)
        valid = False

    if valid:
        path = graph.path(first, second)
    else:
        path = None
    end_time = time.time()

    debug_print('Elapsed time: %f s', (end_time - start_time), debug)

    return path


def make_graph_from_dictionary(filename, word_length, debug):
    """Read in a dictionary of words all the same length and populate the graph.

    :type filename: basestring
    :param filename: the name of the dictionary file to read in

    :rtype a WordGraph populated by the dictionary
    """
    g = WordGraph()
    words = read_in_file(filename, word_length)
    for word in words:
        g.add_word(word)

    debug_print('Added %d words of length %d from %s...',
                (len(words), word_length, filename), debug)

    return g


def read_in_file(filename, word_length):
    """Reads in a file containing a list of words, one word on a line.

    :type filename: basestring
    :type filename: the name of the list of words

    :rtype a list of words
    """
    words = []
    with open(filename) as input_file:
        for word in input_file:
            word = word.rstrip()
            if len(word) == word_length:
                words.append(word)
    return words


def main():
    """Program entry function."""
    debug = False
    word_file = "/usr/share/dict/words"
    for i in range(len(sys.argv)):
        if sys.argv[i] == "-d":
            debug = True
        elif sys.argv[i] == "-f":
            i += 1
            word_file = sys.argv[i]

    first = raw_input('First word: ')
    second = raw_input('Second word: ')

    path = make_ladder(first, second, word_file, debug)

    print 'Path:', path


if __name__ == '__main__':
    main()
