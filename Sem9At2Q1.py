def dia_semana(x):
    if 0 < x <= 7:
        if x == 1:
            return "domingo"
        elif x == 2:
            return "segunda-feira"
        elif x == 3:
            return "terça-feira"
        elif x == 4:
            return "quarta-feira"
        elif x == 5:
            return "quinta-feira"
        elif x == 6:
            return "sexta-feira"
        elif x == 7:
            return "sábado"
    else:
        return "valor inválido"


def main():
    dia = int(input("Escreva um número para ser retornado o seu dia da semana:\n"))
    
    print(dia_semana(dia))
    

if __name__ == '__main__':
    main()