def jogadoresAcimaDaMedia(listaJ, listaA, med):
    listaIndex = []
    listaJogAcMed = []
    listaAltAcMed = []

    for index, i in enumerate(listaA):
        if i > med:
            listaIndex.append(index)
    for i in listaIndex:
        listaJogAcMed.append(listaJ[i])
    for i in listaIndex:
        listaAltAcMed.append(listaA[i])
    for i in range(len(listaIndex)):
        print("Nome do jogador: ",listaJogAcMed[i])
        print(f"Altura do jogador: {listaAltAcMed[i]:.2f}")





def mediaAlt(listaA):
    return sum(listaA)/len(listaA)


def maiorJogador(listaJ, listaA):
    maxA = max(listaA)
    indexJogador = listaA.index(maxA)
    return listaJ[indexJogador], listaA[indexJogador]


def main():
    listaJogadores = []
    listaAlturas = []

    for i in range(12):
        listaJogadores.append(input("Insira o nome do jogador: "))
        listaAlturas.append(float(input("Insira a altura do jogador: ")))


    print("JOGADOR MAIS ALTO DO TIME")
    mJ, mA = maiorJogador(listaJogadores, listaAlturas)
    print("Nome do jogador: ",mJ)
    print(f"Altura do jogador: {mA:.2f}")


    print("ALTURA MÉDIA DO TIME")
    media = mediaAlt(listaAlturas)
    print(f"{media:.2f}")

    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    jogadoresAcimaDaMedia(listaJogadores, listaAlturas, media)


if __name__ == '__main__':
    main()
