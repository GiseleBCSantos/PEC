def estado_civil(x):
    if x == 1:
        return True
    if x == 2:
        return False


def main():
    pessoa = input("Insira o seu nome: ").strip()
    est_civ = int(input("Insira o seu estado civil (1 para casado e 2 para solteiro): "))

    if estado_civil(est_civ) == True:
        conjuge = input("Insira o nome do seu cônjuge: ").strip()
        print(f"A soma de caracteres no seu nome e no nome de seu cônjuge é de: {len(pessoa) + len(conjuge)}.")
    else:
        print(f"A soma de caracteres no seu nome é de: {len(pessoa)}.")



if __name__ == "__main__":
    main()
    
