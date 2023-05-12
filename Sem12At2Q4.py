def eh_primo(x):
    primos = 0
    for i in range(1,x+1):
        if x % i == 0:
            primos+= 1
    return primos <= 2


def main():
    num = int(input("Insira um número para saber se ele é primo ou não :\n"))

    print("É primo." if eh_primo(num)== True else "Não é primo.")

if __name__ == '__main__':
    main()