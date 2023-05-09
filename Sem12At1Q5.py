def calculo(x):
    ano = 1600
    total = x
    while total > x*0.1:
        xmortes = total*0.06
        xnascim = total*0.01
        total = total - xmortes + xnascim
        print(f"Ano: {ano}, número de nascimentos: {xnascim:.0f}, número de mortes: {xmortes:.0f}, total da população: {total:.0f}.")
        ano += 1


def main():
    avesInicio1600 = int(input("Insira a população da ave Dodô no início do ano 1600: \n"))
    calculo(avesInicio1600)
    print("A partir dessa data a população de dodôs caiu para menos de 10% da população original.")


if __name__ == '__main__':
    main()
