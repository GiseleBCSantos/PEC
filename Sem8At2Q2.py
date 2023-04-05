def soma_digitos(x):
    soma = 0
    if x>= 0 and x < 100000:
        x = str(x)
        for i in x:
            i = int(i)
            soma += i
        return soma
    else:
        return -1
            



def main():
    numero = int(input("Insira um número inteiro entre 0 e 100.000 para que seus digitos sejam somados:\n"))

    soma_de_digitos = soma_digitos(numero)

    print(f"A soma dos dígitos foi igual a {soma_de_digitos}")


if __name__ == "__main__":
    main()
    
