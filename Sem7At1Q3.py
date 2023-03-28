def acao(x):
    if x == "V":
        return "Siga"
    elif x == "A":
        return "Atenção"
    elif x == "E":
        return "Pare"
    else:
        return "Entrada inválida"


def main():
    cor_sinal = input("Qual a cor do sinal de trânsito? ").upper()

    print(acao(cor_sinal))


if __name__ == '__main__':
    main()

