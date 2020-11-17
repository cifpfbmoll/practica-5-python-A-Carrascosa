# Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:
# Anchura del rectángulo: 5
# Altura del rectángulo: 3
# *****
# *****
# *****


print("\n<===> Generar un rectangulo <===>\n")

ancho = int(input("1- Inserta el ancho del rectangulo: \n > ")) -1
alto = int(input("2- Inserta lo alto del rectangulo: \n > "))

print("\n")

for i in range(alto):
    for j in range(ancho):
        print("X", end=" ")
    print("X")

print("\n<===> Rectangulo generado <===>\n")