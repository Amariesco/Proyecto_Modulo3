def listar_registros(lista):
    print("\n LISTA DE REGISTROS ")
    if not lista:
        print("\n La lista está vacía.")
    else:
        for i, registro in enumerate(lista, 1):
            print(f"{i}. Nombre: {registro['nombre']} | Edad: {registro['edad']} | Categoría: {registro['categoria']}")

def buscar_registro(lista, nombre_buscar):
    print(f"\nBuscando a: {nombre_buscar}")
    encontrado = False
    for registro in lista:
        if registro['nombre'].lower() == nombre_buscar.lower():
            print(f"Encontrado: \n Nombre: {registro['nombre']} | Edad: {registro['edad']} | Categoría: {registro['categoria']}")
            encontrado = True
            break # Si se encuentra, deja de buscar
    if not encontrado:
        print("\n Usuario no encontrado.")