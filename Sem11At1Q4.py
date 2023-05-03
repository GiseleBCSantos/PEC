def inverter(x):
    if x == 0:
        return "0"
    else:
        novoNum = ''
        while x > 0:
            novoNum += str(x%10)
            x = x //10
    return novoNum


def main():
    numero = int(input("Insira um número para ser invertido: "))
    numInvert = inverter(numero)
    print(f"O número {numero} invertido é {numInvert}.")


if __name__ == '__main__':
    main()
