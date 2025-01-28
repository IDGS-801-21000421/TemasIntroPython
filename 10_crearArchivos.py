
from io import open 
import math


texto=open("archivo.txt", "r")
lectura = texto.readlines()

print(lectura)

print(type(lectura))
print(lectura)

for i in lectura:
    print(i)
    
texto.close()