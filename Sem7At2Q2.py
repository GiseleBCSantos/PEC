def dig_par(x):
    c = 0
    for i in x:
        i = int(i)
        if i % 2 == 0:
            c += 1
    return c




def main():
    numero = input("Insira um número entre 100 e 999: ")

    print(f"{numero} tem {dig_par(numero)} digitos pares.")


if __name__ == '__main__':
    main()
    
