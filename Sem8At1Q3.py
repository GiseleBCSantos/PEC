def leitura_num():
    numeros = []
    for i in range(5):
        n = int(input("Escreva um número inteiro: "))
        numeros.append(n)
    return numeros


def main():
    num = leitura_num()
    num.sort()
    print(f"O maior é o número {num[-1]}.")
    print(f"O menor é o número {num[0]}.")


if __name__ == '__main__':
    main()
