def main():
    L = []
    par = []
    impar = []
    for i in range(20):
        num = int(input("Escreva um número: "))
        L.append(num)
        if num%2 == 0:
            par.append(num)
        else:
            impar.append(num)
    print(f"Lista de números lidos: {L}.")
    print(f"Lista de números pares lidos: {par}.")
    print(f"Lista de números ímpares lidos: {impar}.")


if __name__ == "__main__":
    main()
