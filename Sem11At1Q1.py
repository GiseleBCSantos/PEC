def calculo(x,y):
    valor_att = x
    ano = 0
    while valor_att <  2*x:
        valor_att =valor_att * (1+y/100)
        ano += 1
    return ano

def main():
    dep_inicial = float(input("Insira o seu depósito inicial na poupança: "))
    taxa_juros = float(input("Insira a taxa de juros anual da poupança: "))

    anos = calculo(dep_inicial,taxa_juros)
    print(f"Em {anos} anos você terá o dobro do seu depósito inicial.")


if __name__ == '__main__':
    main()
