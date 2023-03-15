# Como eu fiz:
def inverter(x):
    return x[::-1]

def main():
    num = input("Insira um número entre 1000 e 9999 para ser invertido: ")

    print(f"O numero {num} invertido fica: {inverter(num)}")

if __name__ == '__main__':
    main()

#Como imagino que o professor quer:
def inverter(x):
    u = x % 10
    x = x // 10
    d = x % 10
    x = x // 10
    c = x % 10
    x = x//10
    m = x
    n_i = (u*1000) + (d*100) + (c*10) + m
    return n_i

def main():
    num = int(input("Insira um número entre 1000 e 9999 para ser invertido: "))

    n_i = inverter(num)
    print(f"O inverso de {num} é {n_i}")

if __name__ == '__main__':
    main()
