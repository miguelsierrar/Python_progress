def run():

    fhand = open("mbox-short.txt")

    for line in fhand:
        line = line.rstrip() 
        if line.find("@uct.ac.za") == -1:
            continue
        print(line)

if __name__ == "__main__":
    run()