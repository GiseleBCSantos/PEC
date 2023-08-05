horas = int(input("Insira a quantidade de horas atual: "))
minutos = int(input("Insira a quantidade de minutos atual: "))
segundos = int(input("Insira a quantidade de segundos atual: "))
h = horas*3600
m = minutos * 60
print(f"Passou um total de {h+m+segundos} desde a meia noite.")
