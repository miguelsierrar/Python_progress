def run():

    import string
    fname = input("Enter the file name: ")   
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened: ", fname)
        exit()
        
    histogram = dict()
    for line  in fhand:     
        if line.startswith("From "):
            data = line.split(" ")
            if data[1] not in histogram:
                histogram[data[1]] = 1
            else:
                histogram[data[1]] += 1 

    print(histogram)

if __name__ == "__main__":
    run()