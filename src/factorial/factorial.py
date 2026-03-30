#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 


# --- MODIFICACIÓN SOLICITADA --- 
# Si el largo es menor a 2, significa que no se pasó el número por consola.
if len(sys.argv) < 2:
    entrada = input("No se detectó un argumento. Por favor, ingrese el número: ")
else:
    entrada = sys.argv[1]
# -------------------------------

try:
    if "-" in entrada:
        # Dividimos el rango y convertimos a entero cada parte
        desde, hasta = map(int, entrada.split("-"))
        for i in range(desde, hasta + 1):
            print(f"El factorial de {i} es {factorial(i)}")
    else:
        n = int(entrada)
        print(f"El factorial de {n} es {factorial(n)}")
except ValueError:
    print("Error: Debe ingresar un numero o rango válido (ej. 5 o 4-8).")
