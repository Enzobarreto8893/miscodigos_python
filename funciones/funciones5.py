peso=int(input("ingrese su peso en kilos"))
altura=float(input("ingrese su altura en metros"))

def IMC(peso,altura):
    indice= peso/altura**2 
    return (indice)

if IMC(peso,altura) <  18.5:
     print("Peso inferior al normal")	
if IMC(peso,altura)>18.5 and IMC(peso,altura)< 24.9:
     print("Peso Normal")	
if IMC(peso,altura)>	25.0 and IMC(peso,altura)< 29.9:
    print("Peso superior al normal")
if IMC(peso,altura)> 30.0:
     print("Obesidad")
