# Escribe un programa que pida la anchura y la altura de un rectángulo 
# y lo dibuje de la siguiente manera:
# Anchura del rectángulo: 5
# Altura del rectángulo: 4
# *****
# *   *
# *   *
# *****


print("\n<===> Generar un rectangulo vacio <===>\n")

ancho = int(input("1- Inserta el ancho del rectangulo: \n > "))
alto = int(input("2- Inserta lo alto del rectangulo: \n > "))

print("\n")

for i in range(ancho):
    print("X", end=" ")

for i in range(alto-2):
    print("\nX", end=" ")
    for j in range(ancho-2):
        print(" ", end=" ")
    print("X", end=" ")

print(" ")

for i in range(ancho):
    print("X", end=" ")

print("\n\n<===> Rectangulo vacio generado <===>\n")