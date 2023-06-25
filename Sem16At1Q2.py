def tempAcimMedia(list, med, relacao):
    for i in range(len(list)):
        if list[i] > med:
            print(f"{relacao[i][0]}: {round(list[i],2)}K")


def mediaTempK(list):
    soma = 0
    newMed = []
    for i in range(len(list)):
        if list[i][2] == "K":
            soma += round(list[i][1],2)
            newMed.append(round(list[i][1],2))
        elif list[i][2] == "C":
            soma += round((list[i][1]+ 273.15),2)
            newMed.append(round(list[i][1]+ 273.15,2))
        elif list[i][2] == "F":
            soma += round((((list[i][1] -32) * 5/9) +273.15),2)
            newMed.append(round(((list[i][1] -32) * 5/9) +273.15,2))
    med = soma/len(list)
    return med, newMed


def main():
    listTempAnual = []
    listMeses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
                 "Novembro", "Dezembro"]
    for i in range(12):
        arg =listMeses[i], float(input()), input().upper().strip()
        listTempAnual.append(arg)
    print("TEMPERATURA MÉDIA ANUAL")
    mediaTemperaturaAnual, listaTempKelvin = mediaTempK(listTempAnual)
    print(f"{round(mediaTemperaturaAnual,2)}K")

    print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
    tempAcimMedia(listaTempKelvin, mediaTemperaturaAnual, listTempAnual)

if __name__ == "__main__":
    main()