def eh_impar(num):
    return num % 2 == 1


def main():
    numero = int(input("Insira um número para saber se ele é ímpar ou não (True para ímpar e False para par): "))

    print(eh_impar(numero))


if __name__ == '__main__':
    main()
