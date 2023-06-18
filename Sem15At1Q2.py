def temp():
    temp1 = float(input("Insira a temperatura: ")), input("Insira a escala: ").upper().strip()
    temp2 = float(input("Insira a temperatura: ")), input("Insira a escala: ").upper().strip()
    if temp1[1] == temp2[1]:
        result = temp1[0] + temp2[0], temp1[1]
        return result
    else:
        if temp2[1] == "C":
            newTemp = (temp1[0] - 32) * 5/9
            result = round(temp2[0] + newTemp, 4), temp2[1]
            return result
        else:
            newTemp = (temp1[0] * (9/5))+ 32
            result = round(temp2[0] + newTemp, 4), temp2[1]
            return result


def main():
    somaTemp = temp()
    print("A soma das duas temperaturas é: ",somaTemp)

if __name__ == '__main__':
    main()