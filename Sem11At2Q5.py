def conceito(nota):
    if nota >= 8.5:
        return "A"
    elif nota >= 7:
        return "B"
    elif nota >= 5:
        return "C"
    elif nota >= 4:
        return "D"
    else:
        return "E"
        


def main():
        while True:
            nota = float(input())
            if nota < 0 or nota > 10:
                print("Nota inválida.")
            else:
                break
        conc = conceito(nota)
        print(conc)
        


if __name__ == "__main__":
    main()
