# Escribe un programa que pida un número y calcule su factorial.

print("\n<===> Factorial <===>\n")

num = int(input("1- Inserta un numero: \n > "))
fact = num

print("\n<===> Imprimiendo factorial de %d <===>\n" % (num))

for i in list(range(num)):
    if i != 0:
        fact = i * fact

print("===> El factorial de %d es: %d \n" % (num, fact))