def h(x):
    return x//60

def m(x):
    return x%60

def main():
    minutos = int(input("Insira uma quantidade em minutos para ser feita a conversao em H:M: "))

    print(f"O valor {minutos} convertido em horas é de: {h(minutos)}:{m(minutos)}")

if __name__ == "__main__":
    main()
