def fizzbuzz(x):
    if x%3 == 0 and x%5==0:
        return "FIZZBUZZ"
    elif x % 3 == 0:
        return "FIZZ"
    elif x % 5 == 0:
        return "BUZZ"
    
    else:
        return x


def main():
    numero_int_pos = int(input("Insira um número para retornar FIZZ, BUZZ, FIZZBUZZ ou ele mesmo:\n"))

    fb = fizzbuzz(numero_int_pos)

    print(fb)


if __name__ == "__main__":
    main()
