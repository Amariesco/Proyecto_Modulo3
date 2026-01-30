
from Modulos.datos_basicos import solicitar_informacion
from Modulos.menu import mostrar_menu
from Modulos.gestion_datos import (
    listar_registros, buscar_registro, eliminar_registro, 
    base_datos_usuarios, emails_registrados
)
from Modulos.validaciones import clasificar_edad

base_datos = []

while True: 
    opcion = mostrar_menu()

    if opcion == "1":
        nombre, edad, email, rol = solicitar_informacion()
        
        # Verificar duplicados
        if email in emails_registrados:
            print(f"\n Error: El correo {email} ya existe.")
            continue
            
        categoria_edad = clasificar_edad(edad)
        
        # Guardar usuarios como diccionarios dentro de una lista
        nuevo_usuario = {
            "nombre": nombre,
            "edad": edad,
            "email": email,
            "rol": rol,
            "categoria": categoria_edad,
        }
        
        # Métodos .append() para la lista y .add() para el set
        base_datos.append(nuevo_usuario)
        emails_registrados.add(email)
        print("\n ¡Usuario registrado con éxito!")

    elif opcion == "2":
        listar_registros(base_datos)

    elif opcion == "3":
        nombre_a_buscar = input("\n Escriba el nombre que busca: ")
        buscar_registro(base_datos, nombre_a_buscar)

    elif opcion == "4":
        nombre_a_borrar = input("\n Nombre del usuario a eliminar: ")
        eliminar_registro(base_datos, nombre_a_borrar)

    elif opcion == "5": 
        print("\n Saliendo del sistema.")
        break 

    else:
        print("\n Opción no válida.")
        continue