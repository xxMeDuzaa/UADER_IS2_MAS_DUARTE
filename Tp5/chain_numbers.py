# chain_numbers.py
# Implementación del patrón Chain of Responsibility para números 1..100
# Consumidores: números primos y números pares

class AbstractHandler:
    """Clase base abstracta para todos los manejadores."""

    def __init__(self, nxt):
        """Guarda la referencia al siguiente eslabón de la cadena."""
        self._nxt = nxt

    def handle(self, request):
        """Procesa la solicitud y, si no se maneja, la pasa al siguiente."""
        handled = self.processRequest(request)
        if not handled and self._nxt is not None:
            self._nxt.handle(request)

    def processRequest(self, request):
        """Método que debe ser implementado por las subclases."""
        raise NotImplementedError("Implementar processRequest en la subclase")


class PrimeHandler(AbstractHandler):
    """Manejador que consume números primos."""

    def _is_prime(self, n):
        """Retorna True si n es primo, False en caso contrario."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def processRequest(self, request):
        if self._is_prime(request):
            print(f"PrimeHandler consume el número {request}")
            return True
        return False   # No lo maneja, pasa al siguiente


class EvenHandler(AbstractHandler):
    """Manejador que consume números pares (no primos, porque ya pasó por PrimeHandler)."""

    def processRequest(self, request):
        # Nota: el número ya no puede ser primo porque la cadena primero pasa por PrimeHandler.
        # Si se desea otra prioridad, se puede cambiar el orden de la cadena.
        if request % 2 == 0:
            print(f"EvenHandler consume el número {request}")
            return True
        return False


class DefaultHandler(AbstractHandler):
    """Manejador por defecto: números no consumidos por ningún otro."""

    def processRequest(self, request):
        print(f"DefaultHandler: número {request} NO fue consumido")
        return True   # Siempre maneja, termina la cadena


class Client:
    """Cliente que construye la cadena y lanza las solicitudes."""

    def __init__(self):
        # Construir la cadena: PrimeHandler -> EvenHandler -> DefaultHandler
        default = DefaultHandler(None)
        even = EvenHandler(default)
        prime = PrimeHandler(even)
        self._first = prime

    def process_numbers(self, numbers):
        """Envía cada número al inicio de la cadena."""
        for n in numbers:
            self._first.handle(n)


if __name__ == "__main__":
    # Crear cliente
    client = Client()

    # Lista de números del 1 al 100
    numeros = list(range(1, 101))

    # Procesar
    client.process_numbers(numeros)