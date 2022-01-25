def run():

    fname = input("Enter a file name: ")
    fhand = open(fname)
    total = 0
    counter = 0

    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:"):
            number = line.split(":")[1]
            total = total + float(number)
            counter = counter + 1
    
    average = total / counter
    print(average)

if __name__ == "__main__":
    run()