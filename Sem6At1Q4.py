def main():
    numeros = []
    n1 = int(input("Insira um número: "))
    numeros.append(n1)
    n2 = int(input("Insira um número: "))
    numeros.append(n2)
    n3 = int(input("Insira um número: "))
    numeros.append(n3)
    n4 = int(input("Insira um número: "))
    numeros.append(n4)
    n5 = int(input("Insira um número: "))
    numeros.append(n5)

    maximo = max(numeros)
    minimo = min(numeros)
    media = sum(numeros)/5

    print(f"O maior número digitado foi: {maximo}.")
    print(f"O menor número digitado foi: {minimo}.")
    print(f"A média dos 5 números digitados é de: {media}.")


if __name__ == "__main__":
    main()
