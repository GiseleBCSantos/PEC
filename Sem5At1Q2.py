def area(x):
    return x**2

def perimetro(x):
    return x*4

def main():
    lado = float(input())

    print(f"{area(lado):10.4f}")
    print(f"{perimetro(lado):10.4f}")

__name__ = '__main__'
main()