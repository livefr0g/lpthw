from nose.tools import *
from ex48 import lexicon


def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                            ('direction', 'south'),
                            ('direction', 'east')])

def test_verbs():
    pass

def test_stops():
    pass

def test_nouns():
    pass

def test_numbers():
    pass

def test_errors():
    pass
