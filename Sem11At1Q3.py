def maiorEmenor():
    maiorNum = 0
    menorNum = 10 ** 20
    while True:
        num = int(input("Insira um número: "))
        if num == 0:
            break
        if num > maiorNum:
            maiorNum = num
        if num < menorNum:
            menorNum = num
    if maiorNum == 0 and menorNum == 10**20:
        return "",""
    else:
        return maiorNum, menorNum


def main():
    maior, menor = maiorEmenor()
    if maior != "":
        print(f"O maior número foi: {maior}")
        print(f"O menor número foi: {menor}")


if __name__ == "__main__":
    main()
