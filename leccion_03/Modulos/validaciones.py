# Para verificar si la nota ingresada en valida segun el rango de 7 maximo
def validar_rango_nota(nota):
    if 0 <= nota <= 7.0:
        return True
    else:
        return False

# Para determinar la categoria segun la edad ingresada
def clasificar_edad(edad):
    if edad > 60:
        return "Adulto Mayor"
    elif edad >= 18:
        return "Adulto"
    elif edad > 0:
        return "Menor de edad"
    else:
        return "Edad no válida"
    
# Se cambia el if y else para agregar mas condiciones y resultados en la condicion del alumno
def obtener_estado_academico(promedio):
    if promedio >= 90:
        return "Aprobado con Distinción"
    elif promedio >= 70:
        return "Aprobado"
    elif promedio >= 50:
        return "Recuperación"
    else:
        return "Reprobado"