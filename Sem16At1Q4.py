def mediaVendas(matriz):
    listaMedias = []
    for i in matriz:
        listaMedias.append(sum(i)/len(i))
    return listaMedias



def anoMaisVendas(matriz):
    somas = [0,0,0,0,0,0]
    for index, i in enumerate(matriz):
        for j in range(len(i)):
            somas[j] += matriz[index][j]
    return somas.index(max(somas))+2013, max(somas)



def maisVendido(ano, matriz):
    index = ano - 2013
    maior = 0
    iL = 0
    for indexLinha, linha in enumerate(matriz):
        if linha[index] > maior:
            maior = linha[index]
            iL = indexLinha
    return maior, iL


def criarMatriz(x,y):
    m = []
    for i in range(x):
        linha = []
        for j in range(y):
            linha.append(int(input("Insira um valor:")))
        m.append(linha)
    return m


def main():
    fabric = ["Fiat", "Ford", "GM", "Wolkswagen"]
    matriz = criarMatriz(4,6)

    anoDesejado = int(input("Ano desejado: "))
    maior, fabIndex = maisVendido(anoDesejado, matriz)
    print(f"A fabricante que mais vendeu em {anoDesejado} foi a {fabric[fabIndex]} com {maior} mil unidades.")

    anoCMaisVendas, qntdAnoMaisVendas = anoMaisVendas(matriz)
    print(f"O ano de maior volume geral de vendas foi {anoCMaisVendas} com {qntdAnoMaisVendas} mil unidades.")

    print("A média anual de vendas de cada fabricante entre 2013 e 2018 foi:")
    listaMedias = mediaVendas(matriz)
    for i in range(len(matriz)):
        print(f"A {fabric[i]} vendeu em média {round(listaMedias[i],2)} unidades por ano.")



if __name__ == '__main__':
    main()