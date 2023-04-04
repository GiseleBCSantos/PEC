def leitura_num():
    numeros = []
    for i in range(5):
        n = int(input("Escreva um número inteiro: "))
        numeros.append(n)
    return numeros


def main():
    num = leitura_num()
    media = sum(num) / len(num)
    print(f"A média entre os 5 números inseridos é de: {media:.2f}")
    print("Os seguintes números inseridos são maiores do que a média: ")
    for i in num:
        if i > media:
            print(f"{i:.2f}")


if __name__ == '__main__':
    main()
    
