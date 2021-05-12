# satvocabulary.us to anki

import sys

sys.path.insert(0, "..")
import membean.wordlist as wl

from lxml import etree
from lxml.etree import tostring
import lxml
import lxml.html


def read_file(filename):
    return open(filename).read()


class Word:
    def __init__(self):
        self.name = ""
        self.name2 = None
        self.front = ""
        self.back = ""


def parse_word(tr):
    w = Word()

    try:
        tds = tr.findall("td")

        td0 = tds[0]
        td1 = tds[1]
        td2 = tds[2]
        td3 = tds[3]

        if td0.text is None:
            return None

        if td1.text is None:
            td1 = td1.find("b")

        names = td1.text.split(",")

        w.name = names[0].strip()
        if len(names) > 1:
            w.name2 = names[1].strip()
        w.front = wl.href(w.name, w.name2)
        w.back =  td2.text
        if td3.text:
            w.back = w.back + "<br><br><br>" + td3.text
    except:
        print(tostring(tr))

    return w


def print_word(word):
    print(word.front, end="^")
    print(word.back)


def process_file(filename):
    tree = lxml.html.parse(filename)
    root = tree.getroot()
    elems = root.find_class("WORDLIST")
    for elem in elems:
        for tr in elem.iter("tr"):
            word = parse_word(tr)
            if word:
                print_word(word)


def main():
    test = ["test.htm"]
    importants = ["importants_list.htm"]
    basic1 = ["basic1.htm"]
    basic2 = ["basic2.htm"]
    challenge1 = ["challenge1.htm"]
    challenge2 = ["challenge2.htm"]
    w6000 = ["6000.htm"]

    files = w6000
    for file in files:
        process_file(file)


if __name__ == '__main__':
    main()
