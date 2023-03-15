def eh_consoante(c):
    return c.lower() in "qwrtypsdfghjklzxcvbnm"


def main():
    c = input()
    print(eh_consoante(c))

                   
if __name__ == '__main__':
    main()
