def resultado(x):
    if x % 5 == 0:
        return 9*x + 7
    elif x % 5 == 1:
        return "par" if x % 2 == 0 else "ímpar"
    elif x % 5 == 2:
        return 5 * x**2 - 3*x + 42
    elif x % 5 == 3:
        return x // 10
    else:
        return x**2



def main():
    num = int(input("Insira um número: "))

    print(f"De acordo com a divisão do número por 5 o código teve o seguinte retorno: {resultado(num)}.")



if __name__ == '__main__':
    main()