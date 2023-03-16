''' Escribir una función que reciba el nombre del usuario y después muestre por pantalla
<NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en
mayúsculas y <n> es el número de letras que tienen el nombre.'''




nombres = input("nombre: ")

print(nombres.upper() + " tiene " + str(len(nombres)) + " letras")