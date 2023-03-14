def h(x):
    return x//60

def m(x):
    return x%60

def main():
    minutos = int(input())

    print(f"{h(minutos)}:{m(minutos)}")

__name__ = "__main__"
main()