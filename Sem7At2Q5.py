def ordenação(x):
    x.sort()
    for i in x:
        print(i)
    return


def main():
    num = []
    for i in range(3):
        n = int(input("Insira um número para ser mostrado em ordem crescente: "))
        num.append(n)

    ordenação(num)


if __name__ == '__main__':
    main()
