def comparacao(x,y,z):
    if x != y and y != z and x != z:
        return "Todos os valores são diferentes"
    if x == y and x != z or x == z and x != y or y == z and y != x:
        return "Existem dois valores iguais e um diferente"
    if x == y and y == z and x == z:
        return "Todos os valores são iguais"



def main():
    n1 = int(input("Insira um valor: "))
    n2 = int(input("Insira um valor: "))
    n3 = int(input("Insira um valor: "))


    print(comparacao(n1, n2, n3))



if __name__ == '__main__':
    main()