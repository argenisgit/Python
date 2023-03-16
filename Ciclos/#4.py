'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.
'''


frase = input("Introduzca una frase: ")
letra = input("Introduzca una letra: ")

contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1
        
    print(caracter)