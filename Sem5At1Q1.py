def calcular(x,y,z):
    return 2*x + 5*y - z

def main():
    a = int(input("Insira um valor 'a' para o calculo: "))
    b = int(input("Insira um valor 'b' para o calculo: "))
    c = int(input("Insira um valor 'c' para o calculo: "))

    print(f"O resultado da equação é de {calcular(a,b,c)}")

__name__ = '__main__'
main()
