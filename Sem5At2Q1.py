def eh_vogal(c):
    return c.lower() in "aeiou"


def main():
    c = input()
    print(eh_vogal(c))

                   
if __name__ == '__main__':
    main()
