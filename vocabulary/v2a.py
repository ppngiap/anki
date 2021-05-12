# vocabulary.com to anki

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
        self.front = ""
        self.back = ""


def parse_word(elem):
    w = Word()
    w.name = elem.attrib["word"]
    w.front = wl.href(w.name)

    child = elem.find_class("definition")
    w.back = child[0].text

    child = elem.find_class("example")
    if child is not None:
        # text = child[0].text_content()
        text = tostring(child[0]).decode('utf-8').replace("\n", " ")
        w.back = w.back + " <br><br> " + text

    return w


def print_word(word):
    print(word.front, end="^")
    print(word.back)


def process_file(filename):
    tree = lxml.html.parse(filename)
    root = tree.getroot()
    elems = root.find_class("entry learnable")
    for elem in elems:
        word = parse_word(elem)
        print_word(word)


def main():
    the_wind_in_the_willows = ["The_Wind_In_The_Willows_Ch1_to_3.html", "twinw4to6.html", "twinw7to9.html",
                               "twinw10to12.html"]
    alice_adventures_in_wonderlands = ["aaiw1to3.html", "aaiw4to8.html", "aaiw9to12.html"]
    peter_pan = ["PeterPan1to3.html", "PeterPan4to6.html", "PeterPan7to11.html", "PeterPan12to14.html",
                 "PeterPan15to17.html"]
    a_christmas_carol = ["acc1to2.html", "acc3.html", "acc4to5.html"]
    anne_frank = ["AnneFrank1.htm", "AnneFrank2.htm", "AnneFrank3.htm", "AnneFrank4.htm", "AnneFrank5.htm"]
    the_adventure_of_tom_sawyer = ["taots1.htm", "taots2.htm", "taots3.htm", "taots4.htm", "taots5.htm" ]
    number_the_stars = ["number_the_stars_1.htm", "number_the_stars_2.htm", "number_the_stars_3.htm", "number_the_stars_4.htm", "number_the_stars_5.htm"]
    a_wrinkle_in_time = ["wit1.html", "wit2.html", "wit3.html", "wit4.html"]
    i_robot = ["irobot1.html", "irobot2.html", "irobot3.html", "irobot4.html", "irobot5.html"]
    boy_tales_of_childhood = ["boy1.html", "boy2.html", "boy3.html"]
    julie_of_the_wolves = ["jotw1.html", "jotw2.html", "jotw3.html"]
    the_giver = ["giver1.html", "giver2.html", "giver3.html", "giver4.html", "giver5.html"]

    files = the_giver
    for file in files:
        process_file(file)


if __name__ == '__main__':
    main()
