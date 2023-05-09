def calculo(x,y):
    ano = 0
    if x > y:
        while x > y:
            x += x*0.02
            y += y*0.03
            ano += 1
    return ano


def main():
    pais1 = int(input("Insira a população de um país:\n"))
    pais2 = int(input("Insira a população de um país:\n"))
    if pais1 > pais2:
        anos = calculo(pais1, pais2)
    else:
        anos = calculo(pais2, pais1)
    print(f"A população do país B vai ultrapassar a população do país A em {anos} anos.")


if __name__ == '__main__':
    main()