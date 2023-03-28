def calculo(x):
    if x[2] >= 8 and ((sum(x)/3) + 1) <=10:
      return f"O aluno ganhou 1 ponto na média, e sua média ficou {(sum(x)/3) + 1}"
    elif (sum(x)/3) + 1 > 10:
        return f"O aluno ganhou 1 ponto na média, e sua média ficou {10}"
    else:
        return f" A média do aluno é de {sum(x)/3}"


def main():
    notas = []
    for i in range(3):
        n = float(input("Insira uma nota: "))
        notas.append(n)

    print(calculo(notas))


if __name__ == '__main__':
    main()
