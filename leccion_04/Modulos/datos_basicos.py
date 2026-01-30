# Aquí se declaran las variables y funciones de carga

def solicitar_informacion():
    print("\n Formulario de Registro")
    nombre = input("Ingresa su nombre: ")
    edad = int(input("Ingresa la edad: ")) # Validamos usando int() para numero entero "edad"
    
    return nombre, edad