# Definición de tuplas con información de estudiantes (nombre, edad, calificaciones)
estudiante1 = ("Juan", 18, (85, 90, 92))
estudiante2 = ("María", 17, (75, 80, 88))
estudiante3 = ("Carlos", 19, (90, 85, 95))

# Creación de una lista de tuplas de estudiantes
lista_estudiantes = [estudiante1, estudiante2, estudiante3]

# Función para calcular el promedio de calificaciones de un estudiante
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Función para mostrar detalles de estudiantes y sus promedios de calificaciones
def mostrar_detalles_estudiantes(lista_estudiantes):
    print("Detalles de los estudiantes y sus calificaciones:")
    for estudiante in lista_estudiantes:
        nombre, edad, calificaciones = estudiante
        promedio = calcular_promedio(calificaciones)
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("Calificaciones:", calificaciones)
        print("Promedio de calificaciones:", promedio)
        print()

# Mostrar detalles de estudiantes y sus promedios de calificaciones
mostrar_detalles_estudiantes(lista_estudiantes)
