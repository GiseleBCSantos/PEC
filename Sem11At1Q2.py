def calculo():
    soma = 0
    qntd = 0
    while True:
        num = int(input("Insira um número: "))
        if num != 0:
            soma += num
            qntd += 1
        else:
            break

    if qntd != 0:
        return soma/qntd
    else:
        return ''


def main():
    r = calculo()
    if r != "":
        print(f"A média dos números inseridos é de: {r:.2f}")
    


if __name__ == "__main__":
    main()
