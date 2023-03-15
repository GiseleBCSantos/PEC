def letra():
    return "qwertyuiopasdfghjklzxcvbnm"


def numero():
    return "0123456789"


def main():
    c = input()
    print(c.lower() in letra() or c.lower() in numero())

                   
if __name__ == '__main__':
    main()
