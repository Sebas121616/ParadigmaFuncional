#Iniciamos la función con la que verificamos que la secuencia sea valida, ademas de inicar el generador

def pares (n,m):
    if n <= 0 or n > m or m <= 0:
        #Imprime un error en caso de que se cumpla alguna de las condiciones
        print ("Recuerde ingresar una secuencia valida")
        #Se escribe solo RETURN para que no devuelva nada y acabe el programa
        return

    #El generador se encarga de recorrer todos los numeros de la secuencia
    #Si el residuo de una división entre 2 es igual a 0, hace que yield devuelva ese numero como parte de la secuencia
    for i in range(n, m + 1):
        if i % 2 == 0:
            yield i

#Escribimos por consola de que es el programa

print ("Generador de numeros pares")

#Pedimos n y m por consola, es importante usar INT para que solo acepte numero enteros

n = int(input("Ingrese el numero inicial de la secuencia: "))
m = int(input("Ingrese el numero final de la secuencia: "))

generador = pares(n,m)

print (f"Los numeros pares de la secuencia {n} hasta {m} son: ")

#Imprimimos los numeros pares

for numero in generador:
    print(numero)