def verificacao(listN, listI, listA):

    media = sum(listA)/len(listA)

    for i in range(len(listN)):

        if listI[i] > 13 and listA[i] < round(media,2):

            print(f"O aluno {listN[i]} tem mais de 13 anos e possui altura inferior a media.")

            
def main():

    listaNomes = []

    listaIdades = []

    listaAlturas = []

    for i in range(30):

        listaNomes.append(input("Insira o nome do aluno: "))

        listaIdades.append(int(input("Insira a idade do aluno: ")))

        listaAlturas.append(float(input("Insira a altura do aluno: ")))

    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")

    verificacao(listaNomes, listaIdades, listaAlturas)

    
if __name__ == '__main__':

    main()

