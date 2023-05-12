def fibonacci(x):
    numero1 = 0
    numero2 = 1
    numero3 = numero1 + numero2
    seq  = '0, 1'
    cont = 3
    while cont <= x:
        seq += ', '
        seq+= str(numero3)
        cont+= 1
        numero1 = numero2
        numero2 = numero3
        numero3 = numero1 + numero2
    return seq
    
    
def main():
        qntd = int(input("Insira a quantidade de números de fibonacci que você deseja obter:\n"))
        print(fibonacci(qntd))
 

if __name__  == '__main__' :
    main()    