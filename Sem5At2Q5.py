def simbolo():
    return "qwertyuiopasdfghjklzxcvbnm0123456789"


def main():
    c = input()
    print(c.lower() not in simbolo())

                   
if __name__ == '__main__':
    main()
