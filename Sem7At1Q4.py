
def leitura(x):
    if x in "aeiou":
        return "vogal"
    elif x in "qwrtypsdfghjklzxcvbnm":
        return "consoante"
    elif x in "0123456789":
        return "número"
    else:
        return "símbolo"



def main():
    caractere = input().lower()

    print(leitura(caractere))


if __name__ == '__main__':
    main()

