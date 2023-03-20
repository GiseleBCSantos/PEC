def main():
    numeros = []
    for i in range(0,5):
        n = int(input("Insira um número: "))
        numeros.append(n)

    print(f"O maior número digitado foi: {max(numeros)}.")
    print(f"O menos número digitado foi: {min(numeros)}.")
    print(f"A média dos 5 números digitados é de: {sum(numeros)/5}.")

if __name__ == "__main__":
    main()
