# programa para calcular el area y el perimetro de un circulo

# libreria 
import math 
# -----
# input 
# -----

print ("--------------------------")
print ("area perimetro del circulo")
print ("--------------------------")


r= input("Digite el valor del radio")
r= int(r)

#---------
#procesing 
#---------
a= math.pi*r**2
p= 2*math.pi*r


# output 
print("------------------------------------")
print("-------------resultados-------------")
print("------------------------------------")
print("El área del circulo es: " + str(a))
print("El perímetro del circulo es: " + str(p))
print("------------------------------------")
