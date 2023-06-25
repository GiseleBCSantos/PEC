def maiorElem(matriz):
    maior = 0
    for i in matriz:
        for j in i:
            if j > maior:
                maior = j
    return maior


def menorElem(matriz):
    menor = 2**99
    for i in matriz:
        for j in i:
            if j < menor:
                menor = j
    return menor


def mediaMatriz(matriz):
    sum= 0
    elem = 0
    for i in matriz:
        for j in i:
            sum += j
            elem += 1
    media = sum / elem
    return media

def somaUltCol(m):
    sum = 0
    for i in m:
        sum+= i[-1]
    return sum


def somaPrimLinha(m):
    return sum(m[0])


def criarMatriz(x,y):
    m = []
    for i in range(x):
        linha = []
        for j in range(y):
            linha.append(int(input()))
        m.append(linha)
    return m


def main():
    n = int(input("Quantas linhas a matriz deve ter? "))
    m = int(input("Quantas colunas a matriz deve ter? "))

    matriz = criarMatriz(n,m)

    sumPrimLinha = somaPrimLinha(matriz)
    sumUltLinha = somaUltCol(matriz)
    medMatriz = mediaMatriz(matriz)
    maiorNum = maiorElem(matriz)
    menorNum = menorElem(matriz)

    resposta = sumPrimLinha, sumUltLinha, round(medMatriz,4), menorNum, maiorNum
    print("Na seguinte tuplas teremos, respectivamente, a soma dos elementos da primeira linha, a soma dos elementos da última coluna, a média de todos os elementos, o menor elemento e o maior elemento: ",  resposta)


if __name__ == '__main__':
    main()