def run():

    fhand = open("mbox-short.txt")
    inp = fhand.read()
#    print(len(inp))
    print(inp[:20]) #slicing
    
if __name__ == "__main__":
    run()