# Escribe un programa que pida dos números y escriba qué números entre
# ese par de números son pares y cuáles impares

print("\n\n<===> Detectar numeros par e impares <===>\n\n")

num1 = int(input("1- Inserta un numero: \n > "))
num2 = int(input("\n2- Inserta un numero: \n > "))

print("\n<===> Imprimiendo numeros entre %d y %d <===>\n" % (num1, num2))

for i in list(range(num1, num2)):
    if i != num1:
        if i % 2 == 0:
          print("=> El numero %d es par" % (i))
        else:
          print("=> El numero %d es impar" % (i))

print("\n<===> El bucle ha terminado <===>\n")