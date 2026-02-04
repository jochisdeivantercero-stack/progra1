from nom import*

per1=Nombre("Yuli",18,"Ingenieria quimica")
per2=Nombre("Taylor",18,"Jochis nivel 3")
per3=Nombre("Taylor",18,"Ingeniria en ciencias de la computacion")

print(str(per1))
print(repr(per2))

print(per1+per2)
print(per2*per3)
print(per1==per2) #true
print(per1==per3) #false


