'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''

num = int(input("Introduzca un número entero: "))

for i in range(1, num+1, 2):
    for argenis in range(i, 0, -2):
        print(argenis, end=" ")
    print()