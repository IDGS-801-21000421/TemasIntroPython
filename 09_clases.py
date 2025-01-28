

class OperasBas:
    
    # Declaracion de propiedades
    
    # Para declarar metodo publico
    # public    num1=0


    # Para declarar metodo privado    
    # private    _num1=0

    
    # Para declarar metodo protegido
    # protected     __num1=0
    
    
    # Declaracion de constructor
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
        
    
    # Declaracion de metodos
    
    # Suma
    def suma(self):
        self.num1 + self.num2
        print("La suma es: {}" .format(self.num1 + self.num2))    
    
    # Resta
    def _resta(self):
        self.num1 - self.num2
        print("La resta es: {}" .format(self.num1 - self.num2))    
        

def main():
    # Instancia de la clase
    obj = OperasBas(10, 10)
    
    # Llamada a metodos
    obj.suma()
    obj._resta()
    
if __name__ == "__main__":
    main()