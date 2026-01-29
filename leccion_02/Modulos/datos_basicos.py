# Aquí se declaran las variables y funciones de carga

def solicitar_informacion():
    print("Formulario de Registro")
    nombre = input("Ingresa su nombre: ")
    edad = int(input("Ingresa la edad: ")) # Validamos usando int() para numero entero "edad"
    # Valicion float() para "notas"
    nota1 = float(input("Ingresa la primera calificación (0-100): "))
    nota2 = float(input("Ingresa la segunda calificación (0-100): "))
    
    tipo_usuario = input("Ingresa tipo de usuario (Estudiante/Docente): ")

    return nombre, edad, nota1, nota2, tipo_usuario