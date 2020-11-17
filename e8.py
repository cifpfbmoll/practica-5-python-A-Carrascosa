# Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
# Altura del triángulo: 4
# *
# **
# ***
# ****
# ***
# **
# *


print("\n<===> Generar un triangulo <===>\n")

alto = int(input("1- Inserta lo alto del triangulo: \n > "))
ancho = int(1)
limite = int(1)

print("\n")

for i in range(alto + alto - 1):
    for j in range(ancho):
        print("X", end=" ")
        
    print(" ")
    
    if limite < alto:
        ancho = ancho + 1
        limite = limite + 1
    else:
        ancho = ancho -1

print("\n<===> Triangulo generado <===>\n")