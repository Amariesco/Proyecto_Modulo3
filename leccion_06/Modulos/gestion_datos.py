# Tuplas para Roles del sistema
ROLES_SISTEMA = ('Admin', 'Invitado', 'Usuario') # Tupla inmutable

emails_registrados = set() # Set para evitar duplicados

base_datos_usuarios = [] # Lista para almacenamiento

def listar_registros(lista): # Busca un usuario por nombre
    print("\n LISTA COMPLETA DE REGISTROS ")
    if not lista:
        print("\n La lista está vacía.")
    else:
        for i, registro in enumerate(lista, 1):   
            detalle = "" # Se crea una cadena vacía para ir armando el texto
            for clave, valor in registro.items():             # .items() para obtener clave y valor
                detalle += f"{clave.capitalize()}: {valor.capitalize()} | " # Va sumando al texto con el formato "Clave: Valor | "
            print(f"{i}. {detalle}")


def buscar_registro(lista, nombre_buscar):
    print(f"\nBuscando a: {nombre_buscar}")
    encontrado = False
    for registro in lista:
        # Método .get() para obtener datos de forma segura
        if registro.get('nombre').lower() == nombre_buscar.lower():
            print(f"Encontrado: {registro}")
            encontrado = True
            break 
    if not encontrado:
        print("\n Usuario no encontrado.")

def eliminar_registro(lista, nombre_eliminar):

    for registro in lista:
        if registro.get('nombre').lower() == nombre_eliminar.lower():
            # Eliminar el email del set para que pueda volver a usarse
            email = registro.get('email')
            emails_registrados.remove(email)
            # Eliminar el diccionario de la lista
            lista.remove(registro)
            print(f"\n Registro de {nombre_eliminar} eliminado.")
            return
    print("\n No se encontró el registro para eliminar.")