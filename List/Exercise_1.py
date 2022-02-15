def run():
    
# Write a function called chop that takes a list and modifies it, removing the first and
# last elements, and returns the new list. Then write a function called middle that takes 
# a list and returns a newlist that contains all but the first and last elements

    list_1 = []
    index = 0

    def chop():
        while True:
            number = input("Write any number and press Enter when you finish print Stop\n ")
            list_1.append(number)
            if number == "Stop":
                list_1.remove("Stop")
                list_1.pop(0)
                list_1.pop(index)
                break
            index =+ 1
        print(list_1)

    def middle():
        while True:
            number = input("Write any number and press Enter when you finish print Stop\n ")
            list_1.append(number)
            if number == "Stop":
                list_1.remove("Stop")
                break
        print(list_1[2:4])

    middle()

if __name__ == "__main__":
    run()