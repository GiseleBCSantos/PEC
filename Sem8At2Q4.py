def peso_ideal(x,h):
    if x == 1:
        peso_ideal = (72.7*h)-58
        return peso_ideal
    if x == 2:
        peso_ideal = (62.1*h) -44.7
        return peso_ideal
    else:
        return "erro"


def main():
    altura = float(input("Insira sua altura:\n"))
    sexo = int(input("Insira seu sexo (1 para homem e 2 para mulher):\n"))

    p_i = peso_ideal(sexo, altura)
    print(f"Seu peso ideal é: {p_i:.2f} kg.")
    

if __name__ == "__main__":
    main()
