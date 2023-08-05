#Como eu fiz de inicio:
a =float(input("Insira o primeiro número: "))
b =int(input("Insira o segundo número: "))
print(f"Um exemplo de soma dos números: {a+b:.1f}")
print(f"Um exemplo de concatenação de strings: {str(a)+str(b)}")
print(f"Um exemplo da multiplicação dos números: {a*b}")
print(f"Um exemplo da multiplicação como strings: {str(a)*b}")
print(f"Um exemplo da divisão dos números: {a/b}")
print(f"Um exemplo da divisão inteira dos números: {a//b:.1f}")
print(f"Um exemplo de exponenciação {a**b}")
print(f"Um exemplo de módulo (resto): {a%b}")


#Como eu fiz após entender o objetivo do professor:
a = input("Insira o primeiro número: ")
b = input("Insira o segundo número: ")
print(f"Um exemplo de soma dos números: {float(a)+float(b)}")
print(f"Um exemplo de concatenação de strings: {str(float(a)) + str(b)}")
print(f"Um exemplo da multiplicação dos números: {float(a)* float(b)}")
print(f"Um exemplo da multiplicação como strings: {str(float(a)) * int(b)}")
print(f"Um exemplo da divisão dos números: {float(a) / float(b)}")
print(f"Um exemplo da divisão inteira dos números: {float(a)//float(b)}")
print(f"Um exemplo de exponenciação : {float(a)**float(b)}")
print(f"Um exemplo de módulo (resto): {float(a)%float(b)}")
