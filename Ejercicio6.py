#Iniciamos la función suma con parametro n

def suma (n):
    #Cuando n es 1 devolverá este mismo resultado
    if n == 1:
        return 1
    #De lo contrario hará la suma recursiva
    else:
        return n + suma (n - 1)
    
#Le pedimos al usuario el valor de n, usamos INT porque solo pueden ser numero enteros

n = int(input("Ingrese un numero positivo: "))

if n <= 0:
    #Si el numero n es negativo o 0, no muestra el resultado y se imprime un mensaje
    print("El numero debe ser positivo")
else:
    resultado = suma(n)
    #Imprimos la suma total de la recursion
    print (f"El resultado de su suma es: {resultado}")