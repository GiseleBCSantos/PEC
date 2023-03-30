def dig_par(x):
    x = str(x)
    c = 0
    for i in x:
        i = int(i)
        if i % 2 != 0:
            c += 1
    return c


def main():
    numero = int(input("Insira um número entre 10 e 99: "))

    if numero >= 10 and numero <= 99:
        digitos = dig_par(numero)
        if digitos == 0:
            print("Nenhum dígito é ímpar.")
        elif digitos == 1:
            print("Apenas um dígito é ímpar.")
        else:
            print("Os dois dígitos são ímpares.")
    else:
        print("Número inválido! Tente novamente.")


if __name__ == '__main__':
    main()
