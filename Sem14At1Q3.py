def sumList(list1, list2):
    list3 = []
    for i in range(20):
        list3.append(list1[i] + list2[i])
    return list3


def main():
    listA = []
    listB = []

    for i in range(20):
        listA.append(int(input("Insira um número para a primeira lista: ")))
    for i in range(20):
        listB.append(int(input("Insira um número para a segunda lista: ")))

    listC = sumList(listA, listB)
    print("Primeira lista: ",listA)
    print("Segunda lista: ",listB)
    print("Terceira lista que contêm a soma dos elementos da primeira e segunda lista: ",listC)

if __name__ == '__main__':
    main()
