
# Lista de valores
# range(10) # 0,1,2,3,4,5,6,7,8,9

# Se define un rango de valores con una variable
# x=range(1,11)

# Se define un rango de valores con una variable y un incremento
# y=range(1,11,2)


# Ejercicio 2: Tabla de multiplicar
num1 = int(input("Ingrese el numero de la tabla a multiplicar: "))
numero = range(1, 11)

for num in numero:
    result = num1 * num
    print(num1, "x", num, "=", result)
    
    