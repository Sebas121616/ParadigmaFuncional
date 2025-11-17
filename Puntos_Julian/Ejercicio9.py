def agregar_elemento(set1,elemento):
    set1.add(elemento)
    
def eliminar_elemento(set1,elemento):
    set1.discard(elemento)
    
conjunto ={1,2,3}
agregar_elemento(conjunto,4)
eliminar_elemento(conjunto,2)

resultado = conjunto
print(resultado)
#preguntas a responder:
# 1. ¿que retorna el bloque de codigo?
# R: Retorna el conjunto modificado despues de agregar y eliminar elementos.

# 2. ¿cuantas funciones se declararon?
# R: Se declararon dos funciones: agregar_elemento y eliminar_elemento.

# 3. ¿que imprime en consola?
# R: Imprime el conjunto modificado {1, 3, 4}.
