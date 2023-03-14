def area(x):
    return x**2

def perimetro(x):
    return x*4

def main():
    lado = float(input("Insira um valor para o lado do quadrado: "))

    print(f"A área do quadrado é de: {area(lado):10.4f}")
    print(f"O perimetro do quadrado é de: {perimetro(lado):10.4f}")

__name__ = '__main__'
main()
