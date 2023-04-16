def classif(x):
    score = 0
    for i in x:
        if i.lower() == "s":
            score += 1
    if score == 2:
        return "Suspeito"
    elif 3 <= score <= 4:
        return "Cúmplice"
    elif score == 5:
        return "Assassino"
    else:
        return "Inocente"
  
 
def main():
    resp = ""
    print("Responda com somente S ou N: ")
    resp += input("Telefonou para a vítima ?\n")
    resp += input("Esteve no local do crime ?\n")
    resp += input("Mora perto da vítima ?\n")
    resp += input("Devia para a vítima ?\n")
    resp += input("Já trabalhou com a vítima ?\n")
    
    print(f"Você é: {classif(resp)}.")
    
if __name__ == '__main__':
    main()    