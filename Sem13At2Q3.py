def gerarNumero(x):
    list =[]
    for i in range(x):
        num = float(input(f"Insira a nota do {i+1}° aluno: "))
        list.append(num)
    return list
    
    
def main():
    L = gerarNumero(4)
    indexList = []
    for index,i in enumerate(L):
        if i>=6:
            indexList.append(index)
            
    print("Lista com os índices dos alunos que tem nota igual ou superior a 6: ",indexList)



if __name__  == '__main__' :
    main()         