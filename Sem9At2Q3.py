def data_valida(dia,mes,ano):
    if mes == 1 and dia <= 31:
        return True
    elif mes == 2 and (ano % 4) != 0 and dia <= 28:
        return True
    elif mes == 2 and (ano % 4) == 0 and dia <= 29:
            return True
    elif mes == 3 and dia <= 31:
        return True
    elif mes == 4 and dia <= 30:
        return True
    elif mes == 5 and dia <= 31:
        return True
    elif mes == 6 and dia <= 30:
        return True
    elif mes == 7 and dia <= 31:
        return True
    elif mes == 8 and dia <= 31:
        return True
    elif mes == 9 and dia <= 30:
        return True
    elif mes == 10 and dia <= 31:
        return True
    elif mes == 11 and dia <= 30:
        return True
    elif mes == 12 and dia <= 31:
        return True
    else:
        return False
        

def separar_data(x):
    x = str(x)
    dia = int(x[:2])
    mes = int(x[2:4])
    ano = int(x[4:])
    return dia, mes, ano


def main():
    data = int(input("Insira uma data para que seja feita a verificação se ela é ou não uma data válida (True para data válida e False para data inválida) :\n"))
    
    d, m, a = separar_data(data)
    
    print(data_valida(d, m, a))
    
if __name__ == '__main__':
        main()