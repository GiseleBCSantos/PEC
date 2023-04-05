def soma(x):
    if x % 2 == 0:
        return x + 5
    else:
        return x + 8


def main():
    numero = int(input("Insira um número inteiro para ser somado (Se ele for par será somado com 5, se for impar será somado com 8):\n"))

    print(soma(numero))


if __name__ == "__main__":
    main()
