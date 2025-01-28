class distancia:
    
    def operacion(self):
        self.num1 = int(input("Ingrese el primer valor de la cordenada x1: "))
        self.num2 = int(input("Ingrese el segundo valor de la cordenada y1: "))
        self.num3 = int(input("Ingrese el primer valor de la cordenada x2: "))
        self.num4 = int(input("Ingrese el segundo valor de la cordenada y2: ")) 
        
        # formula
        self.result = ((self.num3 - self.num1)**2 + (self.num4 - self.num2)**2)**0.5
        
        print("La distancia entre los puntos es: {}" .format(self.result))    
        
def main():

    obj = distancia()
    
    obj.operacion()
    
if __name__ == "__main__":
    main()