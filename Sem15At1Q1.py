def compTemp():
    temp1 = float(input("Insira a temperatura: ")), input("Insira a escala: ").upper().strip()
    temp2 = float(input("Insira a temperatura: ")), input("Insira a escala: ").upper().strip()
    if temp1[1] == temp2[1]:
        if temp1[0] > temp2[0]:
            return temp1
        else:
            return temp2
    else:
        if temp1[1] == "C":
            newTemp = 5/9*(temp2[0] - 32)
            if temp1[0] > newTemp:
                return temp1
            else:
                return temp2
        else:
            newTemp = (temp1[0] -32)* (5/9)
            if temp2[0] > newTemp:
                return temp2
            else:
                return temp1


def main():
    maiorTemp = compTemp()
    print("A maior temperatura é: ", maiorTemp)

if __name__ == '__main__':
    main()