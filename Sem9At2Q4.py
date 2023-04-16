def operacao(valor1, valor2, valores):
    total = 0
    if valor1 <= 5: 
        total += valor1 * valores["morango"][0]
    elif valor1 > 5:
        total += valor1 * valores["morango"][1]
    if valor2 <= 5:
        total += valor2 * valores["maca"][0]
    elif valor2 > 5:
        total += valor2 * valores["maca"][1]
    return total*0.9 if total >= 25 or (valor1 + valor2) >= 8 else total
    

def main():
    precos = {"morango": [2.5, 2.2],
                      "maca": [1.8, 1.5]}
    
    
    kg_morang = float(input("Insira a quantidade de kg de morango que você deseja comprar:\n"))
    kg_maca = float(input("Insira a quantidade de kg de maçã que você deseja comprar:\n"))
    
    print(f"Preço total: {operacao(kg_morang, kg_maca, precos):.2f}")
    
    
    
if __name__ == '__main__':
    main()    