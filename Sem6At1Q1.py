def quantidade_de_caracteres(x):
    return len(x)

def main():
    nome = input("Insira seu nome pra saber quantos caracteres ele tem: ").strip()

    print(f"Seu nome tem {quantidade_de_caracteres(nome)} caracteres.")

if __name__ == '__main__':
    main()
