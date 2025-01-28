
# Una lista es una secuencua de elementos 
# Se crean con []



lista = ["Uno", 2, 3.0, 4, True,"Cinco", 33]

print(lista)


print (lista)
print (lista[:])
print (lista[2])
print (lista[-2])
print (lista[0:3])
print (lista[2:])


lista.append("Vargas")
print (lista)

lista.insert(2, "Nadia")

lista.extend(["uno",1.1, "dos"])
print (lista)

lista.remove(33)
print (lista)
lista.pop()
print (lista)


lista2 = ["tres", "cuatro"]
lista3 = lista + lista2
print (lista3)

print(lista2*4)
lista4= [1,2,3,4]
print (lista4.sort())

del lista4[0]
print(lista4)