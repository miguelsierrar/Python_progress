import email

def run():

    fname = input("Enter the file name: ")   
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened: ", fname)
        exit()
        
    email_dict = dict()
    for line  in fhand:     
        if line.startswith("From "):
            data = line.split(" ")
            if data[1] not in email_dict:
                email_dict[data[1]] = 1
            else:
                email_dict[data[1]] += 1 
    
    lst = list()
    for key, val in list(email_dict.items()):
        lst.append((val, key))          #making a list of the  dictionary
    
    lst.sort(reverse = True)      #sorting from biggest values to littlest

    for key, val in lst[:1]:     #only the first one
        print(key, val)

if __name__ == "__main__":
    run()