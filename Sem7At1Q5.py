def calculo(x):
    if x[2] >= 8 and ((sum(x)/3) + 1) <=10:
      return (sum(x)/3) + 1
    elif (sum(x)/3) + 1 > 10:
        return 10
    else:
        return sum(x)/3


def main():
    notas = []
    for i in range(3):
        n = float(input())
        notas.append(n)

    print(calculo(notas))


if __name__ == '__main__':
    main()
