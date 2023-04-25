def eh_par(x):
    return x % 2 == 0


def verificacao():
    par = 0
    impar = 0
    for i in range(3):
        numero = int(input())
        if eh_par(numero):
            par +=1
        else:
            impar += 1
    return par, impar

  
def main():
    pares, impares = verificacao()

    print(f"Dos números inseridos {pares} são pares e {impares} são ímpares") 

            
if __name__ == '__main__':
    main()
