def codigo_numerico(x):
    return ord(x)


def main():
    caractere = input("Insira um caractere para saber seu código numérico: ")

    print(f"O código numérico do seu caractere é: {codigo_numerico(caractere)}")


if __name__ == "__main__":
    main()
