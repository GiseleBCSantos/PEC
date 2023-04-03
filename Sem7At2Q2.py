def dig_par(x):
    x = str(x)
    c = 0
    for i in x:
        if int(i) % 2 == 0:
            c += 1
    return c


def main():
    numero = int(input("Insira um número entre 100 e 999: "))

    if numero >= 100 and numero <= 999:
        print(f"{numero} tem {dig_par(numero)} digitos pares.")
    else:
        print("Número inválido! Tente novamente.")

if __name__ == '__main__':
    main()
    
