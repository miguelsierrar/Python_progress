def run():
    
# Python starts by comparing the first element from each sequence. If they are equal,
# it goes on to the next element, and so on, until it finds elements that differ.
# Subsequent elements are not considered (even if they are really big)

    print((0, 1, 2) < (0, 3, 4))
    
    print((0, 1, 2000000) < (0, 3, 4))

    t1 = (0, 1, 2)
    t2 = (0, 3, 4)
    t3  = (0, 1, 2000)

if __name__ == "__main__":
    run()