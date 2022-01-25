def run():

    fname = input("Enter a file name: ")

    while fname == "na na boo boo":
        print("NA NA BOO BOO TO  YOU - You have been punk´d")
        fname = input("Enter a file name: ")
    
    try:
        fhand = open(fname)
        
    except:
        print("File cannot be oppened: " + fname)
        exit()  #Es necesario siempre escribir exit para saltar el error

    counter = 0

    for line in fhand:
        if line.startswith("Subject: "):
            counter = counter + 1
    
    print("There were", counter, "subject lines in", fname)

if __name__ == "__main__":
    run()