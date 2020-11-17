# Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.


print("\n<===> Sumas <===>\n")

num1 = int(input("1- Inserta un numero: \n > "))
num2 = int(input("2- Inserta un numero: \n > "))
suma = int()

print("\n<===> Imprimiendo suma desde %d hasta %d <===>\n" % (num1, num2))

for i in list(range(num1, num2)):
    suma = suma + i

final= int(num2 + suma)

print("===> La suma total es: %d \n" % (final))