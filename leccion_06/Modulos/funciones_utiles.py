from Modulos.gestion_datos import base_datos_usuarios, emails_registrados

def procesar_baja_usuario(nombre_eliminar): # Para eliminar un usuario.
    global base_datos_usuarios, emails_registrados
    
    usuario_encontrado = None
    
    # Buscar el registro
    for registro in base_datos_usuarios:
        if registro.get('nombre').lower() == nombre_eliminar.lower():
            usuario_encontrado = registro
            break
            
    if usuario_encontrado:
        correo = usuario_encontrado.get('email') # Obtenemos el email antes de borrar el registro
        
        if correo in emails_registrados: 
            emails_registrados.remove(correo) # Eliminamos del SET (para liberar el correo) y de la LISTA
        
        base_datos_usuarios.remove(usuario_encontrado)
        return True
    
    return False

def imprimir_reporte_limpio(lista):
    print("\n REPORTE DE REGISTROS ")
    if not lista:
        print("No hay usuarios en el sistema.")
        return

    for i, registro in enumerate(lista, 1):
        partes = []
        for clave, valor in registro.items():
            partes.append(f"{clave.capitalize()}: {valor}")
        
        print(f"{i}. {' | '.join(partes)}") # join para evitar el '|' al final