# Aquí se declaran las variables y funciones de carga
from Modulos.gestion_datos import ROLES_SISTEMA

def solicitar_informacion():
    print("\n   Formulario de Registro  ")
    nombre = input("Ingresa Nombre: ")
    edad = int(input("Ingresa Edad: "))
    email = input("Ingresa Email: ").lower()
    
    print(f"Roles disponibles: {ROLES_SISTEMA}")
    rol = input("Asigne un Rol: ").capitalize() # capitalize() convierte el primer carácter de una cadena en mayúscula y todos los demás en minúscula
    
    # Validación básica de rol 
    if rol not in ROLES_SISTEMA:
        print("Rol no válido, se asignará 'Usuario' por defecto.")
        rol = "Usuario"
        
    return nombre, edad, email, rol