def ano_mes(a,m,sal,div):
    dividaTotal = div
    while sal > dividaTotal:
        if m ==3:
            sal = sal*1.05
        dividaTotal = dividaTotal*1.15
        m += 1
        if m == 13:
            a += 1
            m = 1
    return a,m


def main():
    anoAtual = 2016
    mesAtual = 10
    salario = float(input("Insira o seu salário atual: "))
    divida = float(input("Insira a sua dívida atual: "))

    anoDestino, mesDestino = ano_mes(anoAtual,mesAtual,salario,divida)

    print(f"Na seguinte data a sua dívida irá superar seu salário: {mesDestino}/{anoDestino}")


if __name__ == '__main__':
    main()
