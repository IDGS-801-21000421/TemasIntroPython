class cinepolis:
    
    def __init__(self):
        self.preciofinaldeventa = 0
        self.precioboleto = 12
    
    def Compra(self):
                
        print("\n-- Compra de Boletos --")
        print("Precio del boleto: $12.00")
        print("Se puede obtener un descuento si cumplen ciertas condiciones")
        nombre = input("\nIngrese su nombre: ")
        personas = int(input("Ingrese el numero de personas: "))
        numboletos = int(input("Ingrese el numero de boletos: "))
        
                  
        while numboletos > 7 * personas:
            print("\n❌ No puede comprar mas de 7 boletos por persona ❌")
            print("1. Cambiar numero de personas")
            print("2. Cambiar numero de boletos")
            
            respuesta = int(input("Ingrese su opción: "))
            
            if respuesta == 1:
                personas = int(input("Ingrese el numero de personas: "))
            elif respuesta == 2:
                numboletos = int(input("Ingrese el numero de boletos: "))

            if numboletos <= 7 * personas:
                break  
            else:
                print("\n⚠️ La cantidad incorrecta, intente de nuevo ⚠️")
   
        if numboletos > 5:
            descuento = 0.15
            total = numboletos * self.precioboleto - (numboletos * self.precioboleto * descuento)
        elif numboletos > 2:
            descuento = 0.10
            total = numboletos * self.precioboleto - (numboletos * self.precioboleto * descuento)
        else:
            total = numboletos * self.precioboleto
            
        while True:
            print("\nSi paga con la tarjeta CINECO de Cinepolis obtendra un 10% de descuento")
            print("1. Efectivo")
            print("2. Tarjeta")
            pago = int(input("Ingrese su metodo de pago: "))
            
            if pago == 1:
                break
            elif pago == 2:
                total = total - (total * 0.10)
                break
            else:
                print("Opcion incorrecta, pruebe de nuevo")
                
        print("\n✅ Compra Registrada")
               
        self.preciofinaldeventa += total

        with open("ticket.txt", "a") as archivo:
            archivo.write(f"Nombre: {nombre}, Personas: {personas}, Boletos: {numboletos}, Total: ${total}\n{'-'*55}\n")      
    
    def TotalFinal(self):
        with open("ticket.txt", "a") as archivo:
            archivo.write(f"\nTotal Final: ${self.preciofinaldeventa}\n")
    
    def Imprimirticket(self):
        with open("ticket.txt", "r") as contenido:
            contenido = contenido.read()
            print("\n-- Ticket Final --")
            print(contenido)
    
    def Reiniciarticket(self):
        with open("ticket.txt", "w") as archivo:
            archivo.write("\n")
            archivo.close()

    def run(self):
        
        self.Reiniciarticket() 
        
        while True:
            print("\n-- ⭐ Bienvenido a Cinepolis ⭐ --")
            print("Seleccione una opcion:")
            print("1. Comprar Boletos")
            print("2. Salir")
    
            op = int(input("\nIngrese su opcion: "))
            
            if op == 1:
                self.Compra()
            elif op == 2:
                self.TotalFinal()
                self.Imprimirticket()
                break
             
def main():
    obj = cinepolis()
    obj.run()

if __name__ == "__main__":
    main()
