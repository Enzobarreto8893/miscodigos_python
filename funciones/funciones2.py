def hora_en_string(hora,minuto,segundo):
    hora= str(hora)
    minuto= str(minuto)
    segundo= str(segundo)
    return (hora + ":" + minuto +":" +segundo  )
print(hora_en_string(10,23,45))
print(hora_en_string(20,3,55))
print(hora_en_string(2,2,10))