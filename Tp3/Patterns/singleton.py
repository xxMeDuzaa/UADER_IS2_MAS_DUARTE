# Straightforward implementation of the Singleton Pattern
#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Singleton
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
class LoggerSans(object):
    def __new__(cls):
        cls._instance = super(LoggerSans,cls).__new__(cls)
        return cls._instance

class Logger(object):
    _instance = None
    nombre= "Melina"
    pepe=0
    def __init__(self):
        pepe=0
        print('Inicializa el objeto')

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

class FactorialCalculator(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FactorialCalculator, cls).__new__(cls)
        return cls._instance

    def factorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("El número debe ser un entero no negativo")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

#*------------------------------------------------------------------
import os
os.system('clear')

print("Genero objetos sin utilizar SINGLETON")
log1s= LoggerSans()
log2s= LoggerSans()

print(log1s)
print(log2s)

print("Genero ahora objetos utilizando SINGLETON")
log1 = Logger()
log1.pepe=log1.pepe+1
print(log1,log1.pepe)
log2 = Logger()
log2.pepe=log2.pepe+1
print(log2,log2.pepe)

print(f"El valor del objeto es {log1} el nombre es {log1.nombre} ")
print(f"El valor del objeto es {log2} el nombre es {log2.nombre} ")

# Ejemplo de uso del FactorialCalculator
calc1 = FactorialCalculator()
calc2 = FactorialCalculator()

print(f"¿Es la misma instancia? {calc1 is calc2}")

print(f"Factorial de 5: {calc1.factorial(5)}")
print(f"Factorial de 0: {calc1.factorial(0)}")
print(f"Factorial de 10: {calc1.factorial(10)}")

# Intentar calcular factorial de un número negativo debería lanzar error
try:
    calc1.factorial(-1)
except ValueError as e:
    print(f"Error: {e}")