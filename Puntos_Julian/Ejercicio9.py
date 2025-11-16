def agregar_elemento(set1,elemento):
    set1.add(elemento)
    
def eliminar_elemento(set1,elemento):
    set1.discard(elemento)
    
conjunto ={1,2,3}
agregar_elemento(conjunto,4)
eliminar_elemento(conjunto,2)

resultado = conjunto
print(resultado)
