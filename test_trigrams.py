import pytest

WORD_BANK_TABLE = [
    (['word1', 'word2', 'word3', 'word4', 'word5', 'word6'],
        {'word1 word2': ['word3'], 'word2 word3': ['word4'],
            'word3 word4': ['word5'], 'word4 word5': ['word6']}),
]


@pytest.mark.parametrize('word_list, result', WORD_BANK_TABLE)
def test_create_word_bank(word_list, result):
    from trigrams import create_word_bank
    assert create_word_bank(word_list) == result
