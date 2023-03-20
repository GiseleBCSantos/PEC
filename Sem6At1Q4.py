def main():
    numeros = []
    n1 = int(input())
    numeros.append(n1)
    n2 = int(input())
    numeros.append(n2)
    n3 = int(input())
    numeros.append(n3)
    n4 = int(input())
    numeros.append(n4)
    n5 = int(input())
    numeros.append(n5)

    maximo = max(numeros)
    minimo = min(numeros)
    media = sum(numeros)/5

    print(maximo)
    print(minimo)
    print(media)


if __name__ == "__main__":
    main()
