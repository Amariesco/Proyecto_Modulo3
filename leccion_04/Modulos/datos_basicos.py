# Aquí se declaran las variables y funciones de carga

def solicitar_informacion():
    print("\n   Formulario de Registro  ")
    nombre = input("\nIngresa Nombre: ")
    edad = int(input("Ingresa Edad: ")) # Validamos usando int() para numero entero "edad"
    
    return nombre, edad