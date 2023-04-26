def calculo(x):
    for i in range(1,25):
        print(f"{i}x de R$ {(x/i):.2f}")


def main():
    valor = float(input("Insira um valor: "))
    calculo(valor)
    


if __name__ == '__main__':
    main()
