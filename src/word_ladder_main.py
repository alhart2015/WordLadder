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


def add_words(graph, word_length, word_file, debug):
    """Adds the words found in word_file of length word_length to graph."""
    debug_print('Adding words of length %d from %s...',
                (word_length, word_file),
                debug)

    first_words = []
    total_words = 0
    with open(word_file) as input_file:
        for word in input_file:
            word = word.rstrip()
            if len(word) == word_length:
                graph.add_word(word)
                total_words += 1
                if len(first_words) < 5:
                    first_words.append(word)

    debug_print('Words added: %d (%s...)', (total_words, first_words), debug)


def make_ladder(first, second, word_file, debug):
    """Return a path from the first word to the second word."""
    debug_print('Creating a word graph from "%s" to "%s"',
                (first, second), debug)

    start_time = time.time()
    graph = WordGraph()
    add_words(graph, len(first), word_file, debug)

    valid = True
    if first not in graph:
        print first, "not in dictionary"
        valid = False
    if second not in graph:
        print second, "not in dictionary"
        valid = False

    if valid:
        path = graph.path(first, second)
        if debug:
            print graph.neighbors(first)
            print graph.neighbors(second)
    else:
        path = None
    end_time = time.time()

    debug_print('Elapsed time: %f s', (end_time - start_time), debug)

    return path


def make_graph_from_dictionary(filename):
    """Read in a dictionary of words all the same length and populate the graph.

    :type filename: basestring
    :param filename: the name of the dictionary file to read in

    :rtype a WordGraph populated by the dictionary
    """
    g = WordGraph()
    words = read_in_file(filename)
    for word in words:
        g.add_word(word)
    return g


def read_in_file(filename):
    """Reads in a file containing a list of words, one word on a line.

    :type filename: basestring
    :type filename: the name of the list of words

    :rtype a list of words
    """
    return []


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

    print 'path:', path


if __name__ == '__main__':
    main()
