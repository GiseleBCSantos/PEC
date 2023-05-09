def nunSorte(x):
    num = 0
    for i in x:
        num += int(i)
    return num


def main():
    data = input("Insira a sua data de nascimento no formato ddmmaaaa:\n")
    numSorte = nunSorte(data)
    print(f"O seu número da sorte é {numSorte}.")


if __name__ == '__main__':
    main()