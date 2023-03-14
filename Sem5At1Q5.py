def inverter(x):
    return x[::-1]

def main():
    num = input("Insira um número para ser invertido: ")

    print(f"O numero {num} invertido fica: {inverter(num)}")

__name__ = '__main__'
main()
