def parte_decimal(numero):
    numero_entero=numero - int(numero)  
    numero_entero=round(numero_entero,5)
    return (numero_entero)
print(parte_decimal(3.14))
print(parte_decimal(35.005))
print(parte_decimal(321.15))