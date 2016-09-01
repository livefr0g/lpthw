from nose.tools import *
from ex48.parser import *
from ex48.lexicon import scan


def test_peek():
    word_list = scan("kill the bear")
    assert_equal(peek(word_list), 'verb')
    assert_equal(peek(None), None)

def test_match():
    word_list = scan("kill the bear")
    word = match(word_list, 'verb')
    assert_equal(word, ('verb', 'kill'))
    word = match(word_list, 'stop')
    assert_equal(word, ('stop', 'the'))
    word = match(word_list, 'noun')
    assert_equal(word, ('noun', 'bear'))
    word = match(word_list, 'noun')
    assert_equal(word, None)

def test_skip():
    word_list = scan("at the bear")
    skip(word_list, 'stop')
    assert_equal(word_list, [('noun', 'bear')])

def test_parse_subject():
    word_list = scan("kill the bear")
    subj = parse_subject(word_list)
    assert_equal(subj, ('noun', 'player'))
    word_list = scan("from asdf")
    assert_raises(ParserError, parse_subject, word_list)

def test_parse_verb():
    word_list = scan("from it kill the bear")
    verb = parse_verb(word_list)
    assert_equal(verb, ('verb', 'kill'))
    word_list = scan("player kill the bear")
    assert_raises(ParserError, parse_verb, word_list)

def test_parse_object():
    word_list = scan("the bear")
    obj = parse_object(word_list)
    assert_equal(obj, ('noun', 'bear'))
    word_list = scan("from north")
    obj = parse_object(word_list)
    assert_equal(obj, ('direction', 'north'))
    word_list = scan("kill the bear")
    assert_raises(ParserError, parse_object, word_list)

def test_parse_sentence():
    word_list = scan("stop at the door")
    result = parse_sentence(word_list)
    assert_equal(result.subject, 'player')
    assert_equal(result.verb, 'stop')
    assert_equal(result.obj, 'door')
    word_list = scan("go to the door")
    assert_raises(ParserError, parse_sentence, word_list)
