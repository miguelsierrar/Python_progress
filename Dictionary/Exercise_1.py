# Write a program that reads the words in word.txt and stores them as keys in a dictionary.
# It doesn´t matter what the values are. Then you can use the in operator as a fast way
# to check whether a string is in the dictionary

def run():
    fhand = open("words.txt") 
    inp = fhand.read()
    revealed_words = repr(inp) #reveals \n
    phrases = revealed_words.split(" ")
    counter = 1
    dict = {}

    for word in phrases:  
       word = word.replace("\\n", " ")
       if (" " in word) == True:
           word_1 = word.split(" ")[0]
           word_2 = word.split(" ")[1]

           dict.update({word_1 : counter})
           counter = counter + 1
           dict.update({word_2 : counter})
       else:
            dict.update({word : counter})
       counter = counter + 1
    
    print(dict)

    guess_word = input("Choose a word and let me see if I find in my really big dictionary: ")
       
    while True:
        if (guess_word in dict) == True:
            print("Very impressive, Nostradamus")
            break
        else:
            print("Keep trying, my fellow")
        guess_word = input("Choose another word: ")

if __name__ == "__main__":
    run()