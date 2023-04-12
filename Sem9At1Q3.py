def verif(x,y):
    return "A sua forma geométrica é um quadrado." if x == y else f"A sua forma geométrica é um retângulo de perímetro {x+x+y+y}, e de área {x*y}."


def main():
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira um número: "))

    print(verif(n1,n2))


if __name__ == '__main__':
    main()