def text(nome, sexo):
    if sexo == 1:
        return f"Ilmo Sr. {nome}"
    elif sexo == 2:
        return f"Ilma Sra. {nome}"
    else:
        return "Sexo inválido"


def main():
    nome = input("Insira seu nome: ").strip()
    sexo = int(input("Insira seu sexo (Digite 1 para Masculino e 2 para Feminino): "))

    print(text(nome, sexo))

if __name__ == '__main__':
    main()


