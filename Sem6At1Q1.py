def quantidade_de_caracteres(x):
    return len(x)

def main():
    nome = input().strip()

    print(quantidade_de_caracteres(nome))

if __name__ == '__main__':
    main()
