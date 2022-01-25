def run():
    fname = input("Enter file name: ")
    try:
        fhand = open(fname)
    
    except:
        print("File cannot be  opened: ", fname)
        exit()
 
    count = 0 
    for line in fhand:
        if line.startswith("Subject:"):
            count = count + 1
    print("There were", count, "subjectt lines in ", fname)

if __name__ == "__main__":
    run()