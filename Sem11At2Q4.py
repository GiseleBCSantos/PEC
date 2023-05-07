def compras():
    total = 0
    while True:
        print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
        compra = input().strip().upper()
        if compra == "X":
            break
        
        if compra == "H":
            total += 5.5
        elif compra == "C":
            total += 6.8
        elif compra == "M":
            total += 4.5
        elif compra == "A":
            total += 7
        elif compra == "Q":
            total += 4

    return total
            


def main():
   total_compras = compras()
   print(f"O total das suas compras foi de R$ {total_compras:.2f}.")
   
    
    
    
if __name__ == "__main__":
    main()
