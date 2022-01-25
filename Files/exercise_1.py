def run():

    fname = input("Enter a file name: ")
    fhand = open(fname)

    for line in fhand:
        print(line.upper())

if __name__ == "__main__":
    run()