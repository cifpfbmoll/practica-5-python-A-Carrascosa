# Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# Altura de un triángulo: 5
#     *
#    ***
#   *****
#  *******
# *********

print ("Vamos a dibujar un triangulo!")

altura=int(input("Ponga la altura del triangulo:"))

for i in range(altura):
    for j in range(altura*2):
        if j <= altura+i and j >= altura-i:
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print(" ")