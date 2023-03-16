'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año
que dura la inversión.
'''

capital = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (%): "))
anios = int(input("Introduce el número de años de la inversión: "))


for ani in range(1, anios + 1):
    capital *= 1 + interes_anual / 100
    print(f"Año {anio}: {capital:.2f} euros")