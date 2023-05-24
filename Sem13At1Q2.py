def lista0(x):
    L = []
    for i in range(x):
        L.append(0)
    return L


def listaCresc(x):
    L = []
    num = 1
    for i in range(x):
        L.append(i + 1)
    return L


def preencher(x):
    L = []
    for i in range(x):
        n = int(input("Insira um número: "))
        L.append(n)
    return L


def preInv(x):
    L = []
    for i in range(x):
        n = int(input("Insira um número: "))
        L.insert(0,n)
    return L


def main():
    tamanho = int(input("Quantos números você quer na sua lista? "))

    print(f"Lista de tamanho {tamanho} preenchida com 0: {lista0(tamanho)}.")

    print(f"Lista de tamanho {tamanho} preenchida em ordem crescente: {listaCresc(tamanho)}.")

    print(f"Lista de tamanho {tamanho} preenchida por valores lidos no teclado: {preencher(tamanho)}.")

    print(f"Lista de tamanho {tamanho} preenchida por valores lidos no teclado em ordem inversa: {preInv(tamanho)}.")


if __name__ == "__main__":
    main()
