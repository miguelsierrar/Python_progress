import email

def run():

    fname = input("Enter the file name: ")   
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened: ", fname)
        exit()
        
    hour_dict = dict()
    for line  in fhand:     
        if line.startswith("From "):
            data = line.split(" ")
            time = data[6]
            hour = time.split(":")
            if hour[0] not in hour_dict:
                hour_dict[hour[0]] = 1
            else:
                hour_dict[hour[0]] += 1  
    hour_list = list()
    for key, val in list(hour_dict.items()):
        hour_list.append((key, val))          #making a list of the  dictionary
    
    hour_list.sort()      #sorting from biggest values to littlest

    for key, val in hour_list:     #only the first one
        print(key, val)

if __name__ == "__main__":
    run()