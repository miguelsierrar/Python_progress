def run():

    lista = []

    def chop():
        while True:
            number = input("Escribe los número que quieras y apreta enter, cuando hayas terminado teclea la palabra Alto: \n ")
            lista.append(number)
            if number == "Alto":
                lista.remove("Alto")
                break
        print(lista)

    def middle():
        while True:
            number = input("Escribe los número que quieras y apreta enter, cuando hayas terminado teclea la palabra Alto: \n ")
            lista.append(number)
            if number == "Alto":
                lista.remove("Alto")
                break
        print(lista[2:4])

    middle()

if __name__ == "__main__":
    run()