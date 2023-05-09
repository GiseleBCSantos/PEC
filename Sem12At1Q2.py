def calculo(x,y):
    mes = 0
    while y <= x:
        mes += 1
        x += x*0.004
        y += y*0.007
    return mes


def main():
    carroHoje = float(input("Insira o preço atual do carro:\n"))
    dinheiro = 10000
    meses = calculo(carroHoje, dinheiro)
    print(f"Você terá dinheiro o suficiente pra comprar o carro em {meses} meses.")


if __name__ == '__main__':
    main()