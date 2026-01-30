
from Modulos.datos_basicos import solicitar_informacion
from Modulos.menu import mostrar_menu
from Modulos.gestion_datos import listar_registros, buscar_registro
from Modulos.validaciones import clasificar_edad


base_datos = []

while True: # True para que el programa y no se detenga
    opcion = mostrar_menu()

    if opcion == "1":
        # Función anterior para pedir datos
        nombre, edad = solicitar_informacion()
        categoria_edad = clasificar_edad(edad)
        
        # Diccionario 
        nuevo_usuario = {
            "nombre": nombre,
            "edad": edad,
            "categoria": categoria_edad,
                }
        base_datos.append(nuevo_usuario)
        print("\n  ¡Usuario registrado con éxito!")

    elif opcion == "2":
        listar_registros(base_datos)

    elif opcion == "3":
        nombre_a_buscar = input("\n   Escriba el nombre que busca: ")
        buscar_registro(base_datos, nombre_a_buscar)

    elif opcion == "4":
        print("\n   Saliendo del sistema.")
        break # Rompe el ciclo while y termina el programa

    else:
        print("\n   Opción no válida, intenta de nuevo.")
        continue # Vuelve al inicio del ciclo