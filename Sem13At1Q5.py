def preList(lista,n, qntd):
    for i in range(qntd):
        num = int(input(f"Insira um número para inserir na lista {n}: "))
        lista.append(num)
    return lista


def main():
    list1 = []
    list2 = []
    list = []
    list1 = preList(list1,1, 25)
    list2 = preList(list2,2, 25)
    for i in range(25):
        list.append(list1[i])
        list.append(list2[i])

    print("Lista 1: ",list1)
    print("Lista 2: ",list2)
    print("Lista com os valores da lista 1 e lista 2 intercalados: ",list)


if __name__ == "__main__":
    main()

