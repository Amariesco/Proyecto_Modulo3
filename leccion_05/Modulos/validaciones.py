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
    
