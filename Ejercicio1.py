def factorial_recursivo(n):
    # El factorial de números negativos no está definido
    if n < 0:
        return "No definido para números negativos"
    
    # Caso Base: 0! = 1. Aquí es donde la recursión se detiene.
    elif n == 0:
        return 1
    
    # Paso Recursivo: n * (n-1)!
    else:
        return n * factorial_recursivo(n - 1)

print("--- Calculadora de Factorial ---")
entrada_usuario = input("Por favor, ingresa un número entero: ")

# Usamos un bloque 'try...except' para asegurarnos de que el usuario
# realmente ingrese un número, y no texto.
try:
    numero = int(entrada_usuario)
    
    resultado = factorial_recursivo(numero)
    
    print(f"El factorial de {numero} es: {resultado}")

except ValueError: #Si no hay numeros enteros marca como error.
    print(f"Error: '{entrada_usuario}' no es un número entero válido.")