from Modulos.menu import mostrar_menu
from Modulos.datos_basicos import solicitar_informacion
from Modulos.validaciones import clasificar_edad
from Modulos.gestion_datos import base_datos_usuarios, emails_registrados, buscar_registro
from Modulos.funciones_utiles import procesar_baja_usuario, imprimir_reporte_limpio # Nuevas funciones

def ejecutar_sistema():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre, edad, email, rol = solicitar_informacion()
            
            if email in emails_registrados:
                print(f"\n Error: El correo {email} ya está en uso.")
                continue
            
            # Creamos el diccionario localmente
            nuevo = {
                "nombre": nombre,
                "edad": edad,
                "email": email,
                "rol": rol,
                "categoria": clasificar_edad(edad)
            }
            
            base_datos_usuarios.append(nuevo)
            emails_registrados.add(email)
            print("\n Registro exitoso.")

        elif opcion == "2":
            # Impresión base de datos
            imprimir_reporte_limpio(base_datos_usuarios)

        elif opcion == "3":
            nombre_buscado = input("\n Nombre a buscar: ")
            buscar_registro(base_datos_usuarios, nombre_buscado)

        elif opcion == "4":
            nombre_a_borrar = input("\n Nombre del usuario a eliminar: ")
            exito = procesar_baja_usuario(nombre_a_borrar) # Nueva función con retorno si se elimina correctamente, o no se encuentra usuario.
            if exito:
                print(f"\n Usuario {nombre_a_borrar} eliminado correctamente.")
            else:
                print("\n No se encontró el usuario.")

        elif opcion == "5":
            print("\n Saliendo del sistema")
            break

if __name__ == "__main__":
    ejecutar_sistema()