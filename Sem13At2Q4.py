def somaCumulativa(lista):
    newList=[]
    testes =[]
    soma = 0
    for index,i in enumerate(lista):
        index +=1
        testes = lista[:index]
        soma = sum(testes)
        newList.append(soma)
        soma = 0
        testes = []
    return newList
    
    
def main():
    list= []
    while True:
        num = int(input("Insira um número (0 para sair): "))
        if num == 0:
            break
        else:
            list.append(num)
            
    print("Nova lista onde cada elemento é a soma dos elementos anteriores da lista original: ",somaCumulativa(list))


if __name__ == '__main__':
    main()