def esta_ordenado(lista):
    ord = []
    for i in lista:
        ord.append(i)
    
    return lista == sorted(ord)
    
    
def main():
    L =[]
    n = int(input("Quantos elementos deseja que sejam lidos? "))
    
    for i in range(n):
        num = input("Insira um elemento: ").strip()
        if num.isalpha():
            L.append(str(num))
        else:
            L.append(float(num))

        
    if esta_ordenado(L):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")


if __name__  == '__main__' :
    main()         