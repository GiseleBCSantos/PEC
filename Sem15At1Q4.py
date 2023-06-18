def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado


def main():
    cidades = carrega_cidades()

    pop = int(input("Insira uma população: "))

    print(f"CIDADES COM MAIS DE {pop} HABITANTES:")
    for i in range(len(cidades)):
        if cidades[i][5] > pop:
            print(f"IBGE: {cidades[i][1]} - {cidades[i][2]}({cidades[i][0]}) - POPULAÇÃO: {cidades[i][5]}")


if __name__ == '__main__':
    main()