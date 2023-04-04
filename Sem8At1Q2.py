def leitura_de_data(x):
    dia = int(input(f"Insira o dia da {x} data: "))
    mes = int(input(f"Insira o mes da {x} data: "))
    ano = int(input(f"Insira o ano da {x} data: "))
    return dia, mes, ano


def calculo_dias(d, m, a):
    m *= 30
    a *= 365
    total = d + m + a
    return total


def main():
    dia1, mes1, ano1 = leitura_de_data("primeira")
    data1 = f"{dia1}/{mes1}/{ano1}"
    dia2, mes2, ano2 = leitura_de_data("segunda")
    data2 = f"{dia2}/{mes2}/{ano2}"

    dias1 = calculo_dias(dia1, mes1, ano1)
    dias2 = calculo_dias(dia2, mes2, ano2)

    if dias1 > dias2:
        print(f" A data {data1} é a mais recente")
    else:
        print(f" A data {data2} é a mais recente")


if __name__ == '__main__':
    main()
    
