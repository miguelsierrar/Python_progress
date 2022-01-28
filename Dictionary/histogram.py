def run():
    word ="brontosaurus"
    counter = dict()

    for letter  in word:
        if letter  not in counter:
            counter[letter] = 1
        else:
            counter[letter]  = counter[letter] + 1
    print(counter) 

if __name__ == "__main__":
    run()