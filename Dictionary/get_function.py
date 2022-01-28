def run():
    counts = {"chuck":1, "annie":42, "jan":100}
    print(counts.get("jan", 0))

################################################

    word ="brontosaurus"
    counter = dict()

    for letter in word:
        counter[letter] = counter.get(letter, 0) + 1 
    print(counter) 

if __name__ == "__main__":
    run()
