#A tuple is a sequence of values much like a list, but are immutable. 
def run():

#Although is not necessary, it is common to enclose tuples in parentheses to help us
# quickly identify tuples when we look at Python code:

    t = ("a", "b", "c", "d", "e")

# To create a tuple wit a single element, you have to include the final comma:

    t1 = ("a",)
    print(type(t1))

# Without the comma Python treats ("a") as a string:

    t2 = ("a")
    print(type(t2))

#Another way  to construct a tuples is  the built-in function tuple

    t = tuple()
    print(t)

# If the argument is a sequence, the result of the call to tuple is a tuple wih elements
# of the sequence:

t = tuple("lupins")
print(t)

# Most list operators also work on tuples

t3 =  ("a", "b", "c", "d", "e")
print(t3[0])

print(t3[1:3])

# You cannot modify elements of the tuple:

# t3[0] = "A"

# But you can replace one tuple with another

t4 = ("A",) + t3[1:]
print(t4)

if __name__ == "__main__":
    run()