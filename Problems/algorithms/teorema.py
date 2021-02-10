"""
Teorema de pitagoras
"""

cateto1, cateto2 = int(input("Cateto 1 : ")), int(input("Cateto 2: "))

hipotenusa =  ((cateto1 ** 2 )  + (cateto2  ** 2)) ** 0.5

print("La hipotenusa es: ", hipotenusa)