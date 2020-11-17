# Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# Altura de un triángulo: 5
#     *
#    ***
#   *****
#  *******
# *********

print("\n<===> Generar un triangulo <===>\n")

alto=int(input("1- Inserta lo alto del triangulo: \n > "))

for i in range(alto):
    for j in range(alto*2):
        if j <= alto+i and j >= alto-i:
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print(" ")

print("\n\n<===> Triangulo generado <===>\n")