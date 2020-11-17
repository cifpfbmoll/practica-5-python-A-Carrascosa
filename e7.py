# Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# Altura del triángulo: 4
# ****
# ***
# **
# *


print("\n<===> Generar un triangulo <===>\n")

alto = int(input("1- Inserta lo alto del triangulo: \n > "))
ancho = int(alto)

print("\n")

for i in range(alto):
    for j in range(ancho):
        print("X", end=" ")
    print(" ")
    ancho = ancho - 1

print("\n<===> Triangulo generado <===>\n")