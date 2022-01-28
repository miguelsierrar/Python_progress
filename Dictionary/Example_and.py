def run():

    import string
    fname = input("Enter the file name: ")   
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened: ", fname)
        exit()
        
    counts = dict()
    for line in fhand:
        line.rstrip() #rstrip method removes any white spaces at the end of the string
        line = line.translate(line.maketrans("", "", string.punctuation)) #The translate() method returns a copy of the string in which all characters have been translated using table (constructed with the maketrans() function in the string module), optionally deleting all characters found in the string deletechars.
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    print(counts)

if __name__ == "__main__":
    run()