'''Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a
una las letras de la palabra introducida empezando por la última.
'''



palabra= input("introduce la palabra:")

for letra in reversed(palabra):
    print(letra)

