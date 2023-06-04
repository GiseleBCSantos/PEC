def elimRepet(lista):
    newList = []
    for i in lista:
        if i not in newList:
            newList.append(i)
        
    return newList


def main():
    list = []
    for i in range(20):
        list.append(int(input("Insira um número: ")))
        
    listaSemRepetidos = elimRepet(list)

    print("Lista sem elementos repetidos: ",listaSemRepetidos)


if __name__== "__main__":
    main()