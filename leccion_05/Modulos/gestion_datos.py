# Tuplas para Roles del sistema
ROLES_SISTEMA = ('Admin', 'Invitado', 'Usuario')

# Sets para evitar duplicados
emails_registrados = set()

base_datos_usuarios = []

def listar_registros(lista):
    print("\n LISTA DE REGISTROS COMPLETOS ")
    if not lista:
        print("\n La lista está vacía.")
    else:
        for i, registro in enumerate(lista, 1):
            claves = list(registro.keys())
            valores = list(registro.values())
            print(f"{i}. Datos: {claves} -> {valores}")

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