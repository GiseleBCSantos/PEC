def extenso(m):
    if m == 1:
        return 'janeiro'
    if m == 2:
        return 'fevereiro'
    if m == 3:
        return 'março'
    if m == 4:
        return 'abril'
    if m == 5:
        return 'maio'
    if m == 6:
        return 'junho'
    if m == 7:
        return 'julho'
    if m == 8:
        return 'agosto'
    if m == 9:
        return 'setembro'
    if m == 10:
        return 'outubro'
    if m == 11:
        return 'novembro'
    if m == 12:
        return 'dezembro'




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

    dia = int(input("Insira um dia: "))
    mes = int(input("Insira um mês: "))
    mesExt = extenso(mes).upper()

    print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mesExt}:")
    for i in range(len(cidades)):
        if cidades[i][3] == dia and cidades[i][4] == mes:
            print(f"{cidades[i][2]}({cidades[i][0]})")


if __name__ == '__main__':
    main()