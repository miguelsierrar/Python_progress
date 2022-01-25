def run():

    fhand = open("mbox-short.txt")
    count = 0

    for line in fhand:
        if line.startswith("From: "):
            print(line)

if __name__ == "__main__":
    run()