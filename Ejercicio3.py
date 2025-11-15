# Una lista de números para el ejemplo
numeros_originales = [10, -5, 0, 8, -1, 3, -20, 7]


# filtramos la lista usando filter y la función lambda 
# para quedarnos solo con los números positivos
numeros_filtrados = filter(lambda x: x > 0, numeros_originales)

# lista de positivos
lista_de_positivos = list(numeros_filtrados)

# imprimimos los resultados
print(f"Lista Original:     {numeros_originales}")
print(f"Lista de Positivos: {lista_de_positivos}")