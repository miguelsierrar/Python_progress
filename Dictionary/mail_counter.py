def run():

    import string
    fname = input("Enter the file name: ")   
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened: ", fname)
        exit()
        
    counts = dict()
    for line  in fhand:        
        if line.startswith("From "):
            data = line.split(" ")
            if data[2] not in counts:
                counts[data[2]] = 1
            else:
                counts[data[2]] += 1 

    print(counts)

if __name__ == "__main__":
    run()