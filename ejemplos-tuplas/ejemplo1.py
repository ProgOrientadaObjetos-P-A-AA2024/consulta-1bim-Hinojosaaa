# Definición de tuplas con información de libros (título, autor, año)
libro1 = ("El principito", "Antoine de Saint-Exupéry", 1943)
libro2 = ("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997)
libro3 = ("Cien años de soledad", "Gabriel García Márquez", 1967)

# Creación de una lista de tuplas de libros
biblioteca = [libro1, libro2, libro3]

# Función para mostrar detalles de libros
def mostrar_detalles_libros(biblioteca):
    print("Detalles de libros en la biblioteca:")
    for libro in biblioteca:
        titulo, autor, año = libro
        print("Título:", titulo)
        print("Autor:", autor)
        print("Año:", año)
        print()

# Mostrar detalles de libros en la biblioteca
mostrar_detalles_libros(biblioteca)
