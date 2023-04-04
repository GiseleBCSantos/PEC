def imc(h, w):
    imc = w/(h**2)
    if imc < 18.5:
        print(f"Seu IMC é: {imc:.2f}")
        return "Abaixo do peso"
    elif imc < 25:
        print(f"Seu IMC é: {imc:.2f}")
        return "Peso normal"
    elif imc < 30:
        print(f"Seu IMC é: {imc:.2f}")
        return "Sobrepeso"
    elif imc < 35:
        print(f"Seu IMC é: {imc:.2f}")
        return "Obeso leve"
    elif imc < 40:
        print(f"Seu IMC é: {imc:.2f}")
        return "Obeso moderado"
    else:
        print(f"Seu IMC é: {imc:.2f}")
        return "Obeso mórbido"


def main():
    peso = float(input("Insira seu peso em kg: "))
    altura = float(input("Insira sua altura em metros: "))


    indice = imc(altura, peso)

    print(indice)


if __name__ == '__main__':
    main()
    
