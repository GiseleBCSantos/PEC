def operacoes(lista):
    novaLista =[]
    for index, i in enumerate(lista):
        if index % 2 == 0:
            novaLista.append(i*3)
        else:
            novaLista.append(i*5)
    return novaLista


def gerarNumero(x):
    list =[]
    for i in range(x):
        num = int(input(f"Insira o {i+1}° número da lista: "))
        list.append(num)
    return list
    
    
def main():
    L = gerarNumero(100)
    L.sort()
    
    newL = operacoes(L)
    print("Nova lista onde, após a ordenação em ordem crescente, os números em índices pares foram multiplicados por 3 e ímpares multiplicados por 5: ", newL)


if __name__  == '__main__' :
    main()         