def conversor(x):
    h = x // 3600
    x = x % 3600
    m = x // 60
    x = x % 60
    s = x
    return h, m, s

def main():
    segundos_totais = int(input())

    horas, minutos, segundos = conversor(segundos_totais)

    print(f"{horas}:{minutos}:{segundos}")


if __name__ == "__main__":
    main()
    
