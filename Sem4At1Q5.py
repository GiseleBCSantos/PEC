altura = float(input("Insira a altura da parede em metros: "))
comprimento = float(input("Insira o comprimento da parede em metros: "))
largura = float(input("Insira a largura da parede em metros: "))
a_piso_s = largura*comprimento
v_s = largura*comprimento*altura
a_parede_s = (2*altura*largura) + (2*altura*comprimento)
print(f"Área do piso da sala: {a_piso_s}m².")
print(f"Volume da sala: {v_s}m³.")
print(f"Área das paredes da sala: {a_parede_s}m².")
