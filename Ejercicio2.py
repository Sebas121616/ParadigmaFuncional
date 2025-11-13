#Se inicia la funcion con 2 parametros, la base y la altura, necesarios para hallar el area de un rectangulo

def calcularArea (base, altura):
    return (base * altura)

#Pedimos los parametros al usuario, se usa FLOAT antes de INPUT porque solo necesitamos numeros, ya sean enteros o decimales

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

#Calculamos el area y lo guardamos en la variable RESULTADO

resultado = calcularArea (base,altura)

#Imprimimos por consola el resultado

print (f"El area del rectangulo con altura {altura} y base {base} es de: {resultado}")