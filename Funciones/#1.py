'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función
debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la
factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
'''

def calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva=21):
  
    total_con_iva = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return round(total_con_iva, 2)

total = calcular_total_con_iva(100)
print(total)
