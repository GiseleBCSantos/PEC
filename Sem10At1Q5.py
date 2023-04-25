def verificacao():
    maiorNumero = 0
    for i in range(100):
        numero = int(input("Escreva um número: "))
        if numero > maiorNumero:
            maiorNumero= numero
    return maiorNumero
        

def main():
    maior = verificacao()
    print(f"O maior número digitado foi: {maior}.")
    
    
if __name__ == '__main__':
    main()
