

def bhashkara(a,b,c):
    x1= float(((-b +(b**2-4*a*c))**1/2)/(2*a))
    x2=float(((-b -(b**2-4*a*c))**1/2)/(2*a))
    return (x1,x2)
print (bhashkara(1,1,1))
print (bhashkara(2,3,1))
print (bhashkara(1,3,1))