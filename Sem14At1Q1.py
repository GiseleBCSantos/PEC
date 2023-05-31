def newSum(list):
    soma = 0
    for i in list:
        soma += i
    return soma


def newMax(list):
    newMax = list[0]
    for i in list:
        if i > newMax:
            newMax = i
    return newMax


def newMin(list):
    newMin = list[0]
    for i in list:
        if i < newMin:
            newMin = i
    return  newMin


def newReverse(obj):
    newObj = obj[::-1]
    return  newObj


def newLen(obj):
    newObj = 0
    for i in obj:
        newObj += 1
    return newObj


def main():
    lista = []
    while True:
        carac = int(input())
        if carac == 0:
            break
        else:
            lista.append(carac)

    print("Lista de números digitados: ", lista)

    print("Nova função para saber o tamanho da lista: ", newLen(lista))

    print("Nova função para reverter a lista: ", newReverse(lista))

    print("Nova função para saber o menor número da lista: ", newMin(lista))

    print("Nova função para saber o maior número da lista: ", newMax(lista))

    print("Nova função para saber a soma da lista: ", newSum(lista))




if __name__ == '__main__':
    main()
