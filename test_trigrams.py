"""Test module for trigrams."""
import pytest

WORD_BANK_TABLE = [
    (['word1', 'word2', 'word3', 'word4', 'word5', 'word6'],
        {'word1 word2': ['word3'], 'word2 word3': ['word4'],
         'word3 word4': ['word5'], 'word4 word5': ['word6']}),
]

ALICE = [('alice', 450, 452)]


@pytest.mark.parametrize('word_list, result', WORD_BANK_TABLE)
def test_create_word_bank(word_list, result):
    """Test the word bank builder function."""
    from trigrams import create_word_bank
    assert create_word_bank(word_list) == result


@pytest.mark.parametrize('filename, num_words, result', ALICE)
def test_generate_trigrams(filename, num_words, result):
    """Test the amount of words generated."""
    from trigrams import generate_trigrams
    assert len(generate_trigrams(filename, num_words).split()) == result
