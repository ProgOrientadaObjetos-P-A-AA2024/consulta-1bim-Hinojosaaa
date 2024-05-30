# Definimos una lista vacía para almacenar los nombres
nombres = []

# Pedimos al usuario que ingrese nombres hasta que escriba "fin"
print("Ingresa los nombres (escribe 'fin' para terminar):")
while True:
    nombre = input("> ")
    if nombre.lower() == 'fin':
        break  # Termina el bucle si se escribe "fin"
    nombres.append(nombre)  # Agrega el nombre a la lista

# Ordenamos los nombres alfabéticamente
nombres.sort()

# Imprimimos los nombres ordenados
print("\nNombres en orden alfabético:")
for nombre in nombres:
    print(nombre)