import sys

class Factorial:
    def __init__(self):
        """Constructor de la clase Factorial."""
        pass

    def _calcular(self, n):
        """Método privado para el cálculo matemático individual."""
        if n < 0: return 0
        if n == 0: return 1
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact

    def run(self, min_val, max_val):
        """Método principal que calcula los factoriales en el rango [min, max]."""
        for i in range(min_val, max_val + 1):
            resultado = self._calcular(i)
            print(f"El factorial de {i} es {resultado}")

# --- Lógica de Interfaz (basada en el programa anterior) ---
if len(sys.argv) < 2:
    entrada = input("Ingrese número o rango (ej. 5, 4-8, -10 o 50-): ")
else:
    entrada = sys.argv[1]

try:
    # Procesamiento de la entrada para obtener min y max
    if "-" in entrada:
        partes = entrada.split("-")
        if partes[0] == "":
            min_n, max_n = 1, int(partes[1])
        elif partes[1] == "":
            min_n, max_n = int(partes[0]), 60
        else:
            min_n, max_n = int(partes[0]), int(partes[1])
    else:
        num = int(entrada)
        min_n, max_n = num, num

    # --- USO DE LA CLASE OOP ---
    mi_factorial = Factorial() # Instanciamos la clase 
    mi_factorial.run(min_n, max_n) # Llamamos al método run 

except ValueError:
    print("Error: Ingrese números válidos.")