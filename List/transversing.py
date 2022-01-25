def run():
    numbers = [17, 123]
    for i in range(len(numbers)): #It creates a list of indices, i.e. (0,2)
        numbers[i] = numbers[i] * 2       

if __name__ == "__main__":
    run()