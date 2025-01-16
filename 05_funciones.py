import os

# Suma
def funcion1():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("El resultado de la suma es: ", num1 + num2)
    resultado = num1 + num2
    input("Preciona enter para continuar")
    
# Resta    
def funcion2():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("El resultado de la resta es: ", num1 - num2)
    resultado = num1 - num2
    input("Preciona enter para continuar")
    
# Multiplicación
def funcion3():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("El resultado de la multiplicación es: ", num1 * num2)
    resultado = num1 * num2
    input("Preciona enter para continuar")
    
# División
def funcion4():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("El resultado de la multiplicación es: ", num1 / num2)
    resultado = num1 / num2
    input("Preciona enter para continuar")


def run():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Seleccione una opción:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
   
        op = int(input("Ingrese su opción: "))
        
        if op == 1:
            funcion1()
        elif op == 2:
            funcion2()
        elif op == 3:
            funcion3()
        elif op == 4:
            funcion4()
        elif op == 5:
            break
             
if __name__ == "__main__":
    run()