#quizlet to membean

def read_lines(filename):
    lines = open(filename).readlines()
    for line in lines:
        words = line.split("\t")
        if len(words) == 2:
            yield words[0], words[1]

fm = "\"<a href=\"\"https://www.membean.com/mywords/%s\"\">%s</a>\""

def main():
    for (key, value) in read_lines("quizlet_level6.txt"):
        key = key.lower()
        print(fm % (key, key), end='\t')
        print(value, end='')

if __name__ == '__main__':
    main()
