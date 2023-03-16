'''Escribir una función que reciba una cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y
minúsculas'''

javi = "lunes"
javi = input("Introduce la contraseña: ")
def clave (password):
    if(javi == password.lower()):
        print(" password  correcto")
    else:
        print("no hay coincidencia")
        
        
        
        
clave("lunes")