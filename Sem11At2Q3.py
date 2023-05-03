def menu():
    while True:
        print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
    
        resposta = int(input())
        if resposta == 1:
            print("1 - Olá. Como vai?")
        elif resposta == 2:
            print("2 - Vamos estudar mais.")
        elif resposta == 3:
            print("3 - Meus Parabéns!")
        elif resposta == 0:
            print("0 - Fim de serviço.")
            break
        else:
            print("Opção inválida.")
        

def main():
    menu()
    
    
if __name__ == "__main__":
    main()
