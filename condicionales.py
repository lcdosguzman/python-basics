#Condicionales

#Existen distintos tipos de Condicionales

#1.- If: se utiliza para ejecutar un bloque de código solo si una condición es verdadera.
edad = 18

if edad >= 18:
    print("Eres mayor de edad")


#2.- if-else  permite ejecutar un bloque de código si la condición es verdadera y otro bloque si es falsa.
edad = 16

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#3.-if-elif-else: se utiliza cuando hay múltiples condiciones que deben ser evaluadas en orden.

puntuacion = 75

if puntuacion >= 90:
    print("A")
elif puntuacion >= 80:
    print("B")
elif puntuacion >= 70:
    print("C")
else:
    print("Reprobado")

#4.- Ternario: Es una forma concisa de expresar una condición en una sola línea.
    
edad = 20
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)

#5 - Condicionales anidados: puedes anidar condicionales para manejar situaciones más complejas.

numero = 7

if numero > 0:
    if numero % 2 == 0:
        print("Número positivo y par")
    else:
        print("Número positivo e impar")
elif numero < 0:
    print("Número negativo")
else:
    print("Número igual a cero")


















