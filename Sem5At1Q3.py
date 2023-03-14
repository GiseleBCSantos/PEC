def aumento(x,y):
    return x* (1+(y/100))

def desconto(x,y):
    return x* (1-(y/100))

def main():
    valor = float(input("Insira um valor para ser feito o cálculo de aumento e desconto: "))
    v_d = float(input("Insira uma porcentagem para o cálculo: "))

    print(f"O aumento do valor de {valor} com {v_d}% foi de: {aumento(valor,v_d):.2f}")
    print(f"O desconto do valor de {valor} com {v_d}% de desconto foi de: {desconto(valor, v_d):.2f}")

__name__ = '__main__'
main()
