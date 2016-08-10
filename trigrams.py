import sys
from random import randint
from random import sample
import io


def create_word_bank(word_list):
    """Create a dictionary with keys of 2 word pairs."""
    word_bank = {}
    for i, word in enumerate(word_list):
        key = word + ' ' + word_list[i + 1]
        if key in word_bank and i < len(word_list) - 2:
            word_bank[key].append(word_list[i + 2])
        elif i < len(word_list) - 2:
            word_bank[key] = [word_list[i + 2]]
        else:
            break
    return word_bank


def create_text(num_words, word_list):
    """This generates the block of computer generated text."""
    word_bank = create_word_bank(word_list)
    rand = randint(0, len(word_list) - 1)
    key = word_list[rand] + ' ' + word_list[rand + 1]
    text = '...' + key
    for i in range(num_words):
        next_word = word_bank[key][randint(0, len(word_bank[key]) - 1)]
        text += ' ' + next_word
        tmp = text.split()
        key = tmp[-2] + ' ' + next_word
    print(text)



def generate_trigrams(filename, num_words):
    """Generates trigram output"""
    f = io.open(filename, encoding='utf-8')
    text = f.read()
    f.close()
    word_list = text.split()
    text = create_text(num_words, word_list)
    print(text)
    return text


def main():
    """Take in filename and run generate_bigrams."""
    if len(sys.argv) != 3:
        print(u'usage: ./trigrams.py file num_words')
        sys.exit(1)
    try:
        num_words = int(sys.argv[2])
    except:
        print(u'num_words must be a positive number')
    else:
        if num_words > 1000 or num_words < 1:
            print(u'num_words must be between 1 and 1000')
            sys.exit(1)
        else:
            filename = sys.argv[1]
            generate_trigrams(filename, num_words)

if __name__ == '__main__':
    main()