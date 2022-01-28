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
            data = line.split(" ")
            if data[1] not in histogram:
                histogram[data[1]] = 1
            else:
                histogram[data[1]] += 1 

    max_number = 0

    for mail in histogram:

        if max_number == 0:
            max_mail = mail
            max_number = histogram[mail]
        
        elif max_number < histogram[mail]:
            max_mail = mail
            max_number = histogram[mail]
    
    print("The number  1 fan is ", max_mail, " with " + str(max_number) + " emails" )

if __name__ == "__main__":
    run()