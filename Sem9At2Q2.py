def separar(num):
    num = str(num)
    frase = ""
    
    for e, i in enumerate(num):
        if len(num) == 1:
            if int(i) == 1:
                frase += f"{extenso(i)} unidade."
            elif int(i) != 0:
                frase += f"{extenso(i)} unidades."
      
        elif len(num) == 2:
            if e == 0:
                if int(i) == 1:
                    frase += f"{extenso(i)} dezena"
                elif int(i) != 0:
                    frase += f"{extenso(i)} dezenas"           
            if e == 1:
                if int(i) == 1:
                    frase += f" e {extenso(i)} unidade."
                elif int(i) != 0:
                    frase += f" e {extenso(i)} unidades."
                else:
                    frase += "."
                    
        elif len(num) == 3:
             if e == 0 and int(num[1]) == 0 and int(num[2]) == 0:
                if int(i) == 1:
                    frase += f"{extenso(i)} centena."
                elif int(i) != 0:
                    frase += f"{extenso(i)} centenas."
             
             elif e == 0:
                if int(i) == 1:
                    frase += f"{extenso(i)} centena"
                elif int(i) != 0:
                    frase += f"{extenso(i)} centenas"           
             if e == 1 and int(num[2]) == 0:
                 if int(i) == 1:
                     frase += f" e {extenso(i)} dezena."
                 elif int(i) != 0:
                     frase += f" e {extenso(i)} dezenas."
             elif e == 1 and num[2] != 0:
                 if int(i) == 1:
                     frase += f", {extenso(i)} dezena"
                 elif int(i) != 0:
                     frase += f", {extenso(i)} dezenas"
             if e == 2:
                  if int(i) == 1:
                      frase += f" e {extenso(i)} unidade."
                  elif int(i) != 0:
                      frase += f" e {extenso(i)} unidades."
                      
    return frase


def extenso(x):
    ext = {"1": "uma", "2": "duas", "3": "três", "4": "quatro", "5": "cinco", "6": "seis", "7": "sete", "8": "oito", "9": "nove"}
    
    return ext[x]


def main():
    num = int(input("Escreva um número positivo e menor do que 1000 para que seja retornado o mesmo em extenso:\n"))
    
    if num >= 1000:
        print("Número inválido.")
        
    print(separar(num))            
             
            
if __name__ == '__main__':
        main()
   