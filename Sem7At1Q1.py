def text(nome, sexo):
    if sexo == 1:
        return f"Ilmo Sr. {nome}"
    elif sexo == 2:
        return f"Ilma Sra. {nome}"
    else:
        return "Sexo inválido"


def main():
    nome = input().strip()
    sexo = int(input())

    print(text(nome, sexo))

if __name__ == '__main__':
    main()


