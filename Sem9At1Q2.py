def menu(x,y, op):
    if op == 1:
        return x + y
    elif op == 2:
        return x - y
    elif op == 3:
        return x * y
    elif op == 4:
        return x / y
    else:
        return "erro"


def main():
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira um número: "))
    operacao = int(input("Qual operação você deseja realizar? \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n"))

    print(f"O resultado da sua operação desejada é de: {menu(n1, n2, operacao)}.")


if __name__ == '__main__':
    main()