# quizlet to anki

import urllib
import sys
sys.path.insert(0, '..')
import membean.wordlist as wl
import urllib3



def href(word):
    if wl.exists(word):
        return wl.href(word)
    else:
        # https://www.ldoceonline.com/dictionary/agog
        # https://www.merriam-webster.com/dictionary/tesseract
        hword = urllib.parse.quote(word)
        h=f"<h2>{word}</h2>"
        vocab = f"<a href=\"\"https://www.spanishdict.com/translate/{hword}\"\">spanishdict</a>"
        header = f"\"{h} {vocab}\""
        return header


def read_quizlet(filename):
    lines = open(filename).readlines()
    for line in lines:
        words = line.split("\t")
        if len(words) == 2:
            yield words[0].lower(), words[1]

if __name__ == "__main__":
    file = "espanol2_para_empezar_3a_quizlet.txt"
    file = "espanol2_4a_AVSR_quizlet.txt"
    file = "espanol2_4a_TOY_quizlet.txt"
    file = "e2c4b_quizlet.txt"
    file = "espanol2_5a_quizlet.txt"
    for word, meaning in read_quizlet(file):
        print(href(word), end=':')
        print(meaning, end='')
