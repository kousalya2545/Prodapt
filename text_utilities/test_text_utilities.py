from text_utilities import unique_word, word_count, reverse_string

def test_word_count():
    assert word_count("Hello World") == 2

def test_word_count_repeated_words():
    assert word_count("") ==0

#Test Unique Words
def test_unique_words():
    assert unique_word("apple apple bannana apple") == ["apple","banana"]

def test_unique_words_single():
    assert unique_word("Hello") == ["Hello"]

def test_unique_word_empty():
    assert unique_word("") == []

#Test string Reversal
def test_reverse_string():
    assert reverse_string("abc") == "cba"

def test_reverse_empty():
    assert reverse_string("") == ""
    
def test_case_sensitive():
    assert unique_word("Hello hello") == ["Hello", "hello"]