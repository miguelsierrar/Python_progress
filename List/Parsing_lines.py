def run():

    fhand = open("mbox-short.txt")
    for line in fhand:
        line =  line.rstrip()
        if not line.startswith("From "):
            continue

        day = line.split()[2]
        print(line)
        print(day)

if __name__ == "__main__":
    run()