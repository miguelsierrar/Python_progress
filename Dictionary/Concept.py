#Dictionary is a set of indices and a set of values
#The order  of items  in a dictionary is unpredictable
#You use the keys to look up the corresponding values

def run():

    eng2sp = {"one":"uno", "two":"dos", "three":"tres"} #eng2sp dictionary
    print(eng2sp)

#   print(eng2sp["four"]) #KeyError, because does not exist "four" key on the eng2sp dictionary
    len(eng2sp) # len() returns the number of key-value

    "one" in eng2sp #The in operator tells you whether something appears as a  key in the dictiionary

    vals = list(eng2sp.values()) #method values returns values as a list
    print(vals)

if __name__ == "__main__":
    run()