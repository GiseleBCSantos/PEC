def calculo(n1,n2):
    primos = 0
    for i in range(n1,n2+1):
        for j in range(1,i+1):
            if i% j ==0:
                primos += 1
        if primos ==2:
            print(i)
        primos = 0
            
    return
    
    
def main():
    num1 = int(input("Insira um número inicial para a contagem de primos:\n"))
    num2 = int(input("Insira um número final para a contagem de primos:\n"))
    
    calculo(num1,num2)

           
                      
if __name__  == '__main__' :
    main()                                            