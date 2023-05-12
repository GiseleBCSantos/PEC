def calculo(x):
    acumul = 1
    if x == 0:
        return 1
    while x != 0:
        acumul *= x
        x -= 1
    return acumul


def main():
    numero = int(input("Insira um número para obter o seu fatorial:\n"))
    fatorial = calculo(numero)
    print(f"O fatorial de {numero} é {fatorial}.")


if __name__== '__main__':
    main()
