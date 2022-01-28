def run():

    counts = {"chuck": 1, "annie": 42, "jan": 100}

    lst = list(counts.keys())
    print(lst)
    lst.sort()           #sort method puts dictionary keys in alphabetical order
    for key in lst:
        print(key, counts[key])

if __name__ == "__main__":
    run()