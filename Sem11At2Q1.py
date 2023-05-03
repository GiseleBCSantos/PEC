def soma():
    soma = 0
    while True:
        num = int(input("Insira um número: "))
        soma += num
        if num == 0:
            break
    return soma


def main():
    sum = soma()
    print(f"A soma dos números inseridos é: {sum}")


if __name__ == '__main__':
    main()
