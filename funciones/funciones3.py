def formateanombre(nombre, apellido, cedula):
    cedula=str(cedula)
    frase= apellido + ", "+  nombre + " tiene el número de cédula " + cedula
    return (frase)
print (formateanombre("enzo","barreto", 45232973))
print (formateanombre("loa","brrto", 453))
print (formateanombre("eo","beto", 452973))