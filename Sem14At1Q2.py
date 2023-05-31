def newCount(lista, num):
    qntd = 0
    for i in lista:
        if i == num:
            qntd += 1
    return qntd


def main():
    lista = []
    while True:
        carac = int(input())
        if carac == 0:
            break
        else:
            lista.append(carac)
    valorAPesquisar = int(input())

    print("Lista de números digitados: ", lista)

    print("Valor a pesquisar: ",valorAPesquisar)

    print("Lista com a nova função que retorna o número de ocorrências do valor na lista: ", newCount(lista, valorAPesquisar))


if __name__ == '__main__':
    main()
