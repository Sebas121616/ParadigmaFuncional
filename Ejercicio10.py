# DATOS A USAR
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

# OPERACIÓN CON "map()" Y "lambda"
resultado = map(lambda x, y, z: x + y + z, lista1, lista2, lista3)

# Convertimos el resultado a lista para imprimirlo
print(list(resultado))

#---RESPUESTA---

#A el resultado es [12, 15, 18]

#B La funcion MAP se encarga de tomar los elementros de las 3 listas 
#  posicion por posicion
#  Por cada posicion, la funcion LAMBDA se encarga de sumar los tres
#  numeros y guardar el resultado en una nueva lista

#  Por ejemplo, en las 3 listas la primera posición de cada lista es 1,4,7. 
#  La funcion se encarga de sumar todos los numeros
#  y guardar el resultado en una nueva lista, en este caso [12]

#  Hace lo mismo con la segunda posicion 2,5,8, [12,15] y tercera posicion 3,6,9, [12,15,18]
#  Por eso el resultado final es [12,15,18]