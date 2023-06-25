from random import *

def somaTodasFiliais(matriz):
    somas = [0,0,0,0]
    for index, i in enumerate(matriz):
        for index2, j in enumerate(i):
            somas[index] += matriz[index][index2]
    return somas


def somaFiliaisAno(m):
    somas = []
    for index, i in enumerate(m):
        linhas = []
        for index, j in enumerate(i):
            linhas.append(sum(j))
        somas.append(linhas)
    return somas


def criarMatriz(x,y,z):
    m = []
    for i in range(x):
        linha = []
        for j in range(y):
            col = []
            for k in range(z):
                col.append(int(input("Insira um valor: ")))
                # col.append(randint(1,100))
            linha.append(col)
        m.append(linha)
    return m


def main():
    matriz = criarMatriz(4, 3, 12)
    anos = [2014,2015,2016,2017]
    filiais = ["Filial 1", "Filial 2", "Filial 3"]
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


    matrizFilialAnos = somaFiliaisAno(matriz)

    matrizAnos = somaTodasFiliais(matrizFilialAnos)


    for index1, i in enumerate(matriz):
        for index2, j in enumerate(i):
            for index3, k in enumerate(j):
                print(f"{anos[index1]};{filiais[index2]};{meses[index3]};{k}")
            print(f"TOTAL {anos[index1]} {filiais[index2].upper()};{matrizFilialAnos[index1][index2]}")
        print(f"TOTAL {anos[index1]} TODAS FILIAIS;{matrizAnos[index1]}")
    print(f"TOTAL PERÍODO TODAS FILIAIS;{sum(matrizAnos)}")

if __name__ == '__main__':
    main()