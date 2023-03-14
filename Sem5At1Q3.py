def aumento(x,y):
    return x* (1+(y/100))

def desconto(x,y):
    return x* (1-(y/100))

def main():
    valor = float(input())
    v_d = float(input())

    print(f"{aumento(valor,v_d):.2f}")
    print(f"{desconto(valor, v_d):.2f}")

__name__ = '__main__'
main()