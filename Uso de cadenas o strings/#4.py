'''Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo
+34-913724710-56). Escribir una función que reciba número de teléfono con este
formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión'''

telefono = input("Introduce un número de teléfono: ")
print('El número de teléfono es ', telefono[4:-3])