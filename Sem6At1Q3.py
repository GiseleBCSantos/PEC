def conversor(x):
    h = x // 3600
    x = x % 3600
    m = x // 60
    x = x % 60
    s = x
    return h, m, s

def main():
    segundos_totais = int(input("Insira o tempo da duração do evento na fábrica: "))

    horas, minutos, segundos = conversor(segundos_totais)

    print(f"Esse evento leva um total de {horas}h:{minutos}m:{segundos}s.")


if __name__ == "__main__":
    main()
