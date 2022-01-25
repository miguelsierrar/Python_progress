def run():

    fhand = open("mbox-short.txt")
    count = 0

    for line in fhand:
        count = count + 1
    
    print("Line Count: ", count)
    
if __name__ == "__main__":
    run()