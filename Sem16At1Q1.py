def maiorValor(x):
    maior = 0
    index = 0
    for i in x:
        for j in i:
            if j > maior:
                maior = j
    for i in x:
        if maior in i:
            posMaior = index, i.index(maior)
            return maior, posMaior
        else:
            index += 1



def menorValor(x):
    menor = 2**99
    index = 0
    for i in x:
        for j in i:
            if j < menor:
                menor = j
    for i in x:
        if menor in i:
            posMenor = index, i.index(menor)
            return menor, posMenor
        else:
            index += 1



def gerarMatriz(x):
    matriz = []
    for i in range(x):
        linha= []
        for j in range(x):
            linha.append(int(input("Insira um elemento: ")))
        matriz.append(linha)
    return matriz

def main():
    n = int(input("Qual a ordem da matriz? "))

    m = gerarMatriz(n)

    mai, posMaior = maiorValor(m)
    print('O maior elemento está na posição: ', posMaior)


    men, posMenor = menorValor(m)
    print('O menor elemento está na posição: ', posMenor)




if __name__ == '__main__':
    main()