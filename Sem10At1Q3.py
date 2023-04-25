def mediaDe100():
    soma= 0
    for i in range(100):
        numero = int(input("Insira um número: "))
        soma += numero
    media = soma / 100
    return media


def main():
    med = mediaDe100()
    print(f"A média dos números inseridos é de {med:.2f}.")
    
   
    
if __name__ == '__main__':
    main()
