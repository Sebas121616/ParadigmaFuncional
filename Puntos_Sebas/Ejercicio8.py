<<<<<<< HEAD
#Usamos una función lambda que se encargue de revisar que un correo tenga @, si es verdadero devuelve True, de lo contrario, False

revisar_correo = lambda correo: "@" in correo

email = input("Ingrese su correo electronico para verificarlo: ")


#Si la funcion lambda devuelve True imprime que el correo es correcto
#De lo contrario imprime que no es correcto
if revisar_correo(email):
    print("Su correo electronico es valido")
else:
=======
#Usamos una función lambda que se encargue de revisar que un correo tenga @, si es verdadero devuelve True, de lo contrario, False

revisar_correo = lambda correo: "@" in correo

email = input("Ingrese su correo electronico para verificarlo: ")


#Si la funcion lambda devuelve True imprime que el correo es correcto
#De lo contrario imprime que no es correcto
if revisar_correo(email):
    print("Su correo electronico es valido")
else:
>>>>>>> 610958ab21db3d71320dedfea10cb085f4a7b536
    print("Su correo electronico no es valido")