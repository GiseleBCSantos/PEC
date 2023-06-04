def atributos(lista):
    qntdNeg = 0
    somaPosit = 0
    for i in lista:
        if i >= 0:
            somaPosit += i
        else:
            qntdNeg += 1
    return qntdNeg, somaPosit


def main():
    list = []
    for i in range(10):
        list.append(int(input("Insira um número: ")))
        
    quantidadeNegativos, somaPositivos = atributos(list)
    
    print("Lista: ",list)
    print("Quantidade de números negativos na lista: ",quantidadeNegativos)
    print("Soma dos números positivos na lista: ",somaPositivos)
       


if __name__== "__main__":
    main()