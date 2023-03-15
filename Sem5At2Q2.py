def eh_letra(c):
    return c.lower() in "qwertyuiopasdfghjklzxcvbnm"


def main():
    c = input()
    print(eh_letra(c))

                   
if __name__ == '__main__':
    main()
