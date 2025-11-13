#Usamos una función lambda que se encargue de revisar que un correo tenga @, si es verdadero devuelve True, de lo contrario, False

revisar_correo = lambda correo: "@" in correo

email = input("Ingrese su correo electronico para verificarlo: ")


#Si la lambda devuelve True lo imprime en pantalla y si no imprimer False en pantalla
if revisar_correo(email):
    print("Su correo electronico es valido")
else:
    print("Su correo electronico no es valido")