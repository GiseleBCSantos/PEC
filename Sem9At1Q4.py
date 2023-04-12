def comparacao(x,y,z):
    dif_1 = abs(y-x)
    dif_2 = abs(z-x)

    return f"O segundo número tem a menor diferença com o primeiro: {dif_1}" if dif_1<dif_2 else f"O terceiro número tem a menor diferença com o primeiro: {dif_2}"

def main():
    n1 = int(input("Insira o primeiro número: "))
    n2 = int(input("Insira o segundo número: "))
    n3 = int(input("Insira o terceiro número: "))

    print(comparacao(n1, n2, n3))


if __name__ == '__main__':
    main()