pi = 3.141592
raio = float(input("Insira um valor para o raio: "))
comp = 2*pi*raio
area_c = pi*raio**2
area_e = 4*pi*raio**2
volume = (4*pi*raio**3)/3
print(f"O comprimento da circunferência é de: {comp:.6f}")
print(f"A área do circulo é de: {area_c:.6f}")
print(f"A área da esfera é de: {area_e:.6f}")
print(f"O volume da esfera é de: {volume:.6f}")
