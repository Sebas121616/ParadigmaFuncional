def decorador(funcion):
    
    # funcion que reempleza a la funcion sumar
    def envoltura(a, b):
        
        # Llama a la función sumar
        resultado = funcion(a, b) 
        
        # adorno
        print(f"El resultado es: {resultado}")
        
    return envoltura

#usamo el decorador que es lo mismo a sumar = decorador(sumar)
@decorador
def sumar(a, b):
    return a + b

@decorador
def resta(a, b):
    return a - b

#llamamos la funcion, que es como llamar a envoltura
sumar(5, -3)
resta(10, 4)
