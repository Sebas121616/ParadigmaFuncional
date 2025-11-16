def identificador(nombre, dni):
    #Dividimos el nombre completo en partes
    partes_nombre = nombre.strip().split() # lo volvemos lista
    
    #Obtenemos el primer nombre
    primer_nombre = partes_nombre[0]
    
    #Obtenemos el apellido y contamos sus letras
    apellido = partes_nombre[-1] #ultimo elemento en la lista
    cantidad_letras = len(apellido)
    
    #Obtenemos los primeros 3 dígitos del DNI
    primeros_tres_dni = dni[:3]
    
    #Creamos el ID
    return f"{primer_nombre}{cantidad_letras}{primeros_tres_dni}"


while True:
    
    nombre = input("\nIngrese el nombre completo del socio: ").strip()
    
    # si no coloca nombre, salimos del bucle
    if not nombre:
        print("\nProcesamiento finalizado")
        break
        
    # ciclo de validacion de DNI
    while True:
        dni = input(f"Ingrese el DNI (7 u 8 dígitos) para {nombre}: ").strip()
        
        # Validamos si es un numero y si tiene 7 u 8 dígitos
        if dni.isdigit() and (len(dni) == 7 or len(dni) == 8):
            break # si es valido, salimos del ciclo
        else:
            print("El DNI debe ser numérico y tener 7 u 8 dígitos. Intente de nuevo.")
    
    # generamos el identificador
    id_socio = identificador(nombre, dni)
    
    print(f"Identificador generado: {id_socio}")