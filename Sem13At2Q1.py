def multiplica_constante(lista, constante):
    novaLista = []
    for i in lista:
        novaLista.append(i*constante)
    return novaLista
    
    
def main():
    L =[]
    while True:
        num = int(input("Insira um número (0 para parar o programa): "))
        if num == 0:
            break
        else:
            L.append(num)
    const = int(input("Insira um valor para a constante: "))
    
    
    newL = multiplica_constante(L, const)
    print("Nova lista onde cada valor lido é multiplicado pela constante: ",newL)
    
    
if __name__  == '__main__' :
    main()         