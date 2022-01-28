def run():

    fname = input("Enter the file name: ")   
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened: ", fname)
        exit()
        
    histogram = dict()
    for line  in fhand:     
        if line.startswith("From "):
            mail = line.split(" ")[1]
            domain = mail.split("@")[1]
            if domain not in histogram:
                histogram[domain] = 1
            else:
                histogram[domain] += 1

    print(histogram)
if __name__ == "__main__":
    run()