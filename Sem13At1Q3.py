def letras(x):
    L = []
    cont = 0
    if x == 0:
        return L, cont
    else:
        for i in range(x):
            letra = input("Insira uma letra: ")[0]
            if letra.lower() in "aeiou":
                cont += 1
            else:
                L.append(letra)
        return L, cont


def notas(x):
    L = []
    cont = 0
    acum = 0
    if x == 0:
        return L, 0
    else:
        for i in range(x):
            n = float(input("Insira uma nota: "))
            L.append(round(n,1))
            acum += n
            cont += 1
        return L, acum/cont


def invert(x):
    L = []
    if x == 0:
        return L
    else:
        for i in range(x):
            n = float(input("Insira um número: "))
            n = round(n,4)
            L.insert(0,n)
        return L


def main():
    tamanho = int(input("Quantos espaços você deseja na sua lista? "))

    print(f"Lista de tamanho {tamanho} com valores lidos pelo teclado na ordem inversa: {invert(tamanho)}.")

    nota, media = notas(tamanho)
    print(f"Lista de notas registradas: {nota}.")
    if media == 0:
        print("SEM NOTAS.")
    else:
        print(f"A média das notas é de: {media:.1f}")

    listLetras, vogais = letras(tamanho)
    print(f"Quantidade de vogais {vogais}.")
    print(f"Lista com as consoantes lidas: {listLetras}.")




if __name__ == "__main__":
    main()

