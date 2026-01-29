# Punto de entrada donde se llama a las funciones

# Importar la función desde nuestro módulo
from Modulos.datos_basicos import solicitar_informacion

nombre, edad, n1, n2 = solicitar_informacion() # Llamar a la función para capturar datos


# Calculamos un promedio simple para utilizar operadores aritméticos
promedio = (n1 + n2) / 2


# Comprobar si aprobó y si es mayor de edad para utilizar operadores de comparación y lógicos
aprobado = promedio >= 4.0
es_mayor = edad >= 18

# Crear el registro usando un DICCIONARIO
registro_usuario = {
    "nombre": nombre,
    "edad": edad,
    "promedio": promedio,
    "estado": "Aprobado" if aprobado else "Reprobado", 
}

# Guardar en una lista
base_datos = []
base_datos.append(registro_usuario)

# Mostrar resultados con f-strings para ejecutar código junto al print
print("\n--- RESUMEN DEL REGISTRO ---")
print(f"Usuario: {registro_usuario['nombre']}")
print(f"Promedio obtenido: {registro_usuario['promedio']}")
print(f"¿Es mayor de edad?: {es_mayor}") # Imprime falso en caso de no ser mayor
print(f"Estado final: {registro_usuario['estado']}")