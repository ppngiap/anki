# manage membean wordlist

import os.path as op

words = []


def read_words():
    global words
    filepath = op.join(op.dirname(__file__), "wordlist_high_school.txt")
    text = open(filepath).read()
    words = text.split()
    words = sorted(words)
    # print(words)
    # print(len(words))


def exists(word):
    try:
        words.index(word)
        return True
    except ValueError:
        return False


def href(word, word2 = None):
    membean = f"<a href=\"\"https://www.membean.com/mywords/{word}\"\">membean</a>"
    vocab  = f"<a href=\"\"https://www.vocabulary.com/dictionary/{word}\"\">vocabulary</a>"
    image  = f"<a href=\"\"https://www.google.com/search?q={word}&source=lnms&tbm=isch\"\">image</a>"
    google  = f"<a href=\"\"https://www.google.com/search?q=define+{word}\"\">google</a>"
    # https: // www.google.com / search?q = clamber & source = lnms & tbm = isch
    if (exists(word)):
        if word2:
            fm = f"\"<h2>{word}, {word2}</h2>{membean} {vocab} {image} {google}\""
        else:
            fm = f"\"<h2>{word}</h2>{membean} {vocab} {image} {google}\""
    else:
        if word2:
            fm = f"\"<h2>{word}, {word2}</h2>{vocab} {image} {google}\""
        else:
            fm = f"\"<h2>{word}</h2>{vocab} {image} {google}\""

    return fm


if len(words) == 0:
    read_words()

if __name__ == "__main__":
    read_words()
    print("exists(abate) = %s" % exists("abate"))
    print("exists(abaty) = %s" % exists("abaty"))
    print(href('abate'))
    print(__file__)
    print(op.dirname(__file__))
