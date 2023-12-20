#Bucles

#1-For

#Recorriendo una lista
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)

#Usando un rango
for numero in range(1, 5):
    print(numero)


#2-While
contador = 0

while contador < 5:
    print(contador)
    contador += 1


#Interrupciones y Continuaciones
#En ambos bucles, puedes utilizar las palabras clave break y continue para controlar el flujo del bucle.
    

#Ejemplo Break
for numero in range(10):
    if numero == 5:
        break
    print(numero)

