def indexMaior(lista):
    maxNum = max(lista)
    for index, i in enumerate(lista):
        if i == maxNum:
            return index


def main():
    list = []
    for i in range(10):
        list.append(int(input("Insira um número inteiro: ")))
       
    maiorNum = max(list)
    indexMaiorNum = indexMaior(list)
    
    print("Lista: ",list)
    print("Maior elemento da lista: ",maiorNum)
    print("Posição em que o maior elemento da lista se encontra: ",indexMaiorNum)


if __name__== "__main__":
    main()