def main():
    L = []
    for i in range(10):
        n = int(input("Insira um número: "))
        L.append(n)
    print("Números inseridos: ",L)
    print("Soma dos números inseridos: ",sum(L))
    
    produto = 1
    for i in L:
        produto *= i
    print("Produto dos números inseridos: ",produto)


if __name__ == "__main__":
    main()
