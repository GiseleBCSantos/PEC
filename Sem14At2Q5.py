def unirListas(l1,l2):
    listC = []
    for i in range(len(l1)):
        if l1[i] not in listC:
            listC.append(l1[i])
    for i in range(len(l2)):
        if l2[i] not in listC:
            listC.append(l2[i])
    return listC


def criarList(x):
    l = []
    for i in range(x):
        l.append(int(input(f"Insira um número: ")))
    return l


def main():
    listA = criarList(10)        
    listB = criarList(10)
       
    print("União das duas listas sem elementos repetidos: ",unirListas(listA,listB))



if __name__== "__main__":
    main()