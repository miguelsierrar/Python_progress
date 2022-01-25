def run():

    numlist = list()
    while(True):

        inp = input("Enter a number: ")
        if inp == "done": break
        value = float(inp)
        numlist.append(value)
    
    average =  sum(numlist) / len(numlist)
    print("Average: ", average)

if __name__ == "__main__":
    run()