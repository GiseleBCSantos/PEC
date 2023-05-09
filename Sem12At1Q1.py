def  calculo(x):
    min = 1
    lebre = 10
    if x == 0:
        return 0
    while lebre <= x:
        lebre += 10
        min +=1
        x += 1
    return min


def main():
    metrosTartFrent = int(input("Quantos metros a tartaruga saiu a frente da lebre?\n"))
    minutos = calculo(metrosTartFrent)
    print(f"Levará {minutos} minutos para a lebre alcançar a tartaruga.")


if __name__ == '__main__':
    main()