# Escribe un programa que escriba a los siguientes número (la separación entre número
# es para facilitar cuántos números se deben escribir en cada bucle) y en el que la
# función range que utilices tenga un ÚNICO argumento y que el valor de este se corresponda
# con el número de elementos que aparecen en la lista ( por Ejemplo, para la primera lista range (10)).

lista = list(range(10))

for i in lista:
    print(i + 1, end=" ")
print("\n <===> Terminado Bucle 1 <===>\n")

for i in lista:
    print(i * 2 + 2, end=" ")
print("\n <===> Terminado Bucle 2 <===>\n")

for i in lista:
    print(i * 2 + 20, end=" ")
print("\n <===> Terminado Bucle 3 <===>\n")



for i in list(range(6)):
    print(i * 4 + 10, end=" ")
print("\n <===> Terminado Bucle 4 <===>\n")



for i in list(range(9)):
    print(40 - (i * 5), end=" ")
print("\n <===> Terminado Bucle 5 <===>\n")
