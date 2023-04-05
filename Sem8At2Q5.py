def status(x):
    if x == "A" or x == "B" or x == "C":
        return "aprovado"
    else:
        return "reprovado"


def conceito(x):
    if x >= 9:
        c = "A"
    elif x >= 7.5:
        c = "B"
    elif x >=6:
        c = "C"
    elif x >=4:
        c = "D"
    else:
        c = "E"
    return c


def media_final(list, exerc):
    media_final = (list[0] + list[1]* 2 + list[2]*3 + exerc)/7
    return media_final

def main():
    matricula = input("Insira sua matricula:\n")
    notas = []
    
    for i in range(3):
        n = float(input("Insira sua nota: "))
        notas.append(n)

    media_exercicios = float(input("Insira a média das notas obtidas nos exercícios: "))

    m_f = media_final(notas, media_exercicios)

    conc = conceito(m_f)

    stat = status(conc)

    print(f"Sua matrícula é: {matricula}")
    print(f"Sua média final é: {m_f:.2f}")
    print(f"Seu conceito é: {conc}")
    print(f"Você está {stat}")

    












if __name__ == "__main__":
    main()
