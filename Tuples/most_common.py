def run():
    
    import string

    fhand = open("Romeo_full.txt")
    counts = dict()
    for line in fhand:
        line = line.translate(str.maketrans("","", string.punctuation)) #Removes punctuation
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:  #dicttionary word counter
                    counts[word] = 1    #if word new on dictionary count 1
            else:
                counts[word] += 1       #if word already on dictionary plus 1 on counter
    lst = list()
    for key, val in list(counts.items()):
        lst.append((val, key))          #making a list of the  dictionary
    
    lst.sort(reverse = True)      #sorting from biggest values to littlest

    for key, val in lst[:10]:     #only the first 10 words
        print(key, val)
if __name__ == "__main__":
    run()