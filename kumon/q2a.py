# quizlet to anki

import sys
sys.path.insert(0, '..')

import membean.wordlist as wl


def href(word):
    if wl.exists(word):
        return wl.href(word)
    else:
        # https://www.ldoceonline.com/dictionary/agog
        # https://www.merriam-webster.com/dictionary/tesseract
        h=f"<h2>{word}</h2>"
        longman = f"<a href=\"\"https://www.ldoceonline.com/dictionary/{word}\"\">longman</a>"
        mw = f"<a href=\"\"https://www.merriam-webster.com/dictionary/{word}\"\">merriam-webster</a>"
        vocab = f"<a href=\"\"https://www.vocabulary.com/dictionary/{word}\"\">vocabulary</a>"
        header = f"\"{h} {vocab}\""
        return header


def read_quizlet(filename):
    lines = open(filename).readlines()
    for line in lines:
        words = line.split("\t")
        if len(words) == 2:
            yield words[0].lower(), words[1]

if __name__ == "__main__":
    for word, meaning in read_quizlet("quizlet_kumon_G.txt"):
        print(href(word), end=':')
        print(meaning, end='')
