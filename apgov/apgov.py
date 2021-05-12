# quizlet to anki

def title(word):
    return f"<h2>{word}</h2>"


def read_quizlet(filename):
    lines = open(filename).readlines()
    for line in lines:
        words = line.split("\t")
        if len(words) == 2:
            yield words[0], words[1]


if __name__ == "__main__":
    for word, meaning in read_quizlet("quizlet_apgov4.txt"):
        print(title(word), end='^')
        print(meaning, end='')
