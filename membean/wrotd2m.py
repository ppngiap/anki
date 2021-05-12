# word of the day to anki

from lxml import etree
import lxml
import lxml.html


class WrotdTarget(object):

    def __init__(self):
        self.wrotd = False
        self.divCount = 0

    def start(self, tag, attrib):
        try:
            class_attr = attrib["class"]
        except KeyError:
            class_attr = ""
        if tag == "div":
            if class_attr.startswith("archived-wrotd"):
                self.wrotd = True
                print("start %s %r" % (tag, dict(attrib)))
                self.divCount = 0
            self.divCount += 1

    def end(self, tag):
        if tag == "div":
            self.divCount -= 1
            if self.wrotd and self.divCount == 0:
                print("end %s" % tag)

    def data(self, data):
        if self.wrotd:
            print("data %r" % data)

    def comment(self, text):
        if self.wrotd:
            print("comment %s" % text)

    def close(self):
        if self.wrotd:
            print("close")
        return "closed!"


def read_file(filename):
    return open(filename).read()


class MembeanRoot:
    def __init__(self):
        self.date = ""
        self.name = ""
        self.meaning = ""
        self.summary = ""
        self.href = ""


def parse_membean_root(elem):
    mr = MembeanRoot()
    for child in elem.iterchildren():
        tag = child.tag
        if tag == "h4":
            mr.date = child.text
        elif tag == "h2":
            mr.name = child.text
        elif tag == "h3":
            mr.meaning = child.text
        elif tag == "a":
            mr.href = child.attrib["href"]
        elif tag == "p":
            child.attrib.clear()
            mr.summary = lxml.html.tostring(child).decode()
    return mr


def dump_membean_root(mr):
    print(mr.date)
    print(mr.name)
    print(mr.meaning)
    print(mr.href)
    print(mr.summary)


def print_membean_root(mr):
    fm_front = "\"<a href=\"\"%s\"\"><h1>%s</h1></a>\""
    print(fm_front % (mr.href, mr.name), end="\t")

    fm_back = "\"<strong>%s</strong><br><br>%s\""
    summary = mr.summary.replace("\"", "\"\"").replace("\n", "")
    print(fm_back % (mr.meaning, summary))


def process_file(filename):
    tree = lxml.html.parse(filename)
    root = tree.getroot()
    elems = root.find_class("archived-wrotd")
    for elem in reversed(elems):
        mr = parse_membean_root(elem)
        print_membean_root(mr)
        print()


def main():
    files = ["wr6.htm", "wr5.htm", "wr4.htm", "wr3.htm", "wr2.htm", "wr1.htm"]
    for file in files:
        process_file(file)


if __name__ == '__main__':
    main()
