def a_vista(x):
    total = x * (1 - 0.09)
    return total


def pagamento_5_vezes(x):
    total = x
    parcela = total / 5
    return parcela


def pagamento_10_vezes(x):
    total = x * (1 + 0.17)
    parcela = total / 10
    return parcela


def main():
    valor = float(input("Insira o preço da etiqueta do produto: "))

    valor_a_vista = a_vista(valor)
    pag_5_vezes = pagamento_5_vezes(valor)
    pag_10_vezes = pagamento_10_vezes(valor)

    print(f"Para quem pagar à vista, a compra será de R$ {valor_a_vista:.2f}.")
    print(f"Para quem pagar parcelado em 5 vezes, o valor da parcela será de R$ {pag_5_vezes:.2f}.")
    print(f"Para quem pagar parcelado em 10 vezes, o valor da parcela será de R$ {pag_10_vezes:.2f}.")


if __name__ == "__main__":
    main()
