def calculo(x):
    cont = 1
    h = 0
    while cont <= x:
        h += 1/cont
        cont += 1
    return h


def main():
    numero = int(input("Insira um número para ser aplicado a formula de H:\n"))
    h1 = calculo(numero)
    print(f"Resultado: {h1:.4f}")


if __name__== '__main__':
    main()
