def prodEscalar(l1,l2):
    listProd =[]
    strProdEsc = ""
    for i in range(5):
        listProd.append(l1[i] * l2[i])
        strProdEsc += f"({l1[i]} x {l2[i]}) "
        if i < 4:
            strProdEsc += "+ "
        else:
            strProdEsc += "= "
    prodEscalar = sum(listProd)      
    strProdEsc += f"{prodEscalar}"
    return strProdEsc 


def criarList(x):
    l = []
    for i in range(x):
        l.append(int(input("Insira um número: ")))
    return l


def main():
    listA = criarList(5)        
    listB = criarList(5)
    produtoEscalar = prodEscalar(listA,listB)
       
    print("Primeira lista: ",listA)
    print("Segunda lista: ",listB)
    print("Produto escalar das duas listas: ",produtoEscalar)



if __name__== "__main__":
    main()