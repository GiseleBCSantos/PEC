def leitura_de_data(x):
    dia = int(input("Insira o dia " + x + ": "))
    mes = int(input("Insira o mes " + x + ": "))
    ano = int(input("Insira o ano " + x + ": "))
    return dia, mes, ano

def calculo_dias(d, m, a):
    m *= 30
    a *= 365
    total = d + m + a
    return total

def main():
    dia_atual, mes_atual, ano_atual = leitura_de_data('atual')
    dia_nasc, mes_nasc, ano_nasc = leitura_de_data('de nascimento')

    dias_atuais = calculo_dias(dia_atual, mes_atual, ano_atual)
    dias_nasc = calculo_dias(dia_nasc, mes_nasc, ano_nasc)
    diferenca_dias = dias_atuais - dias_nasc

    idade_em_anos = diferenca_dias // 365
    print(f"Você tem {idade_em_anos} anos")


if __name__ == '__main__':
    main()
