def calculo():
    soma = 0
    maior = 0
    menor = 10**20
    qntd = 0
    while True:
        num = int(input("Insira um número: "))
        if num == 0:
            break
        else:
            soma += num
            qntd += 1
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if qntd == 0:
        return '','','',''
    else:
        media = soma / qntd
        return qntd, media, maior, menor


def main():
    quantidade, med, maiorNum, menorNum = calculo()
    if quantidade != '':

        print(f"Foram inseridos {quantidade} números.")
        print(f"A média dos números inseridos é de: {med:.2f}")
        print(f"O menor número inserido: {menorNum}.")
        print(f"O maior número inserido: {maiorNum}.")


if __name__ == '__main__':
    main()
