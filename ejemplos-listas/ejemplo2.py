# Pedimos al usuario que ingrese la cantidad de números
num_numeros = int(input("Ingrese la cantidad de números: "))

# Creamos una lista vacía para almacenar los números
numeros = []

# Pedimos al usuario que ingrese los números y los agregamos a la lista
print("Ingrese los números uno por uno:")
for i in range(num_numeros):
    num = float(input(f"Número {i+1}: "))
    numeros.append(num)

# Calculamos el promedio de los números
promedio = sum(numeros) / len(numeros)

# Mostramos el promedio
print(f"El promedio de los números ingresados es: {promedio}")