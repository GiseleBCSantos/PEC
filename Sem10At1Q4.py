def gerador():
    text= ''
    for i in range(10,1001,10):
        text += str(i) 
        if i != 1000:
            text += ", "
        else: 
            text += "."
    return text


def main():
    sequencia = gerador()
    print("O programa irá exibir uma sequencia de números que começa em 10 e termina em 1000 com um intervalo de 10 números.")
    print(sequencia)
    
    
    
if __name__=='__main__':
    main()
