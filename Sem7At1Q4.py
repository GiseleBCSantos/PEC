def leitura(x):
    if x[0] in "aeiou":
        return "vogal"
    elif x[0] in "qwrtypsdfghjklzxcvbnm":
        return "consoante"
    elif x[0] in "0123456789":
        return "número"
    else:
        return "símbolo"



def main():
    caractere = input("Escreva um caractere para saber se ele é vogal, consoante, número ou símbolo: ").lower()

    print(leitura(caractere))


if __name__ == '__main__':
    main()
    
