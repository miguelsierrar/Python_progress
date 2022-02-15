import re

def run():

    hand = open("mbox-short.txt")
    for line in hand:
        line = line.rstrip()
        if re.search('From: ', line):
            print(line)

if __name__ == "__main__":
    run()