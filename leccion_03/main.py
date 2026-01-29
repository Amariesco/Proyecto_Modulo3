# Punto de entrada donde se llama a las funciones

# Importar las funciónes desde módulos datos basicos y validaciones
from Modulos.datos_basicos import solicitar_informacion
from Modulos.validaciones import validar_rango_nota, clasificar_edad, obtener_estado_academico

nombre, edad, n1, n2 = solicitar_informacion() # Llamar a la función para capturar datos


if not (validar_rango_nota(n1) and validar_rango_nota(n2)):
    print("\nError: Una de las calificaciones ingresadas no es válida (debe ser 0-100).")
else:
    # Procesar si las notas son válidas
    promedio = (n1 + n2) / 2
    
    # Uso de lógica condicional y lógica anidada
    categoria_edad = clasificar_edad(edad)
    estado_final = obtener_estado_academico(promedio)
    
    # Registro usando un DICCIONARIO
    registro_usuario = {
        "nombre": nombre,
        "edad": edad,
        "categoria": categoria_edad,
        "promedio": promedio,
        "estado": estado_final
    }

# Mostrar resultados con f-strings para ejecutar código junto al print
print("\n" + "="*30)
print("RESUMEN DEL REGISTRO")
print("="*30)
print(f"Usuario: {registro_usuario['nombre']}")
print(f"Categoría: {registro_usuario['categoria']}")
print(f"Promedio: {registro_usuario['promedio']:.2f}")
print(f"Resultado: {registro_usuario['estado']}")
print("="*30)