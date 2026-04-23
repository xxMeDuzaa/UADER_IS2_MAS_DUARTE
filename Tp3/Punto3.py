#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación - Factory Method
#*------------------------------------------------------------------------

class Hamburguesa:
    """Clase que representa una hamburguesa con diferentes métodos de entrega"""
    
    def __init__(self, metodo_entrega: str):
        """
        Inicializa la hamburguesa con el método de entrega especificado
        
        Args:
            metodo_entrega: Puede ser "mostrador", "retiro" o "delivery"
        """
        self.metodo_entrega = metodo_entrega
    
    def entregar(self):
        """Imprime el método de entrega de la hamburguesa"""
        if self.metodo_entrega == "mostrador":
            print(f"Hamburguesa entregada en MOSTRADOR")
        elif self.metodo_entrega == "retiro":
            print(f"Hamburguesa RETIRADA por el cliente")
        elif self.metodo_entrega == "delivery":
            print(f"Hamburguesa enviada por DELIVERY")
        else:
            print(f"Método de entrega '{self.metodo_entrega}' no válido")


#*------------------- Código de prueba -------------------
if __name__ == "__main__":
    print("=" * 50)
    print("PEDIDOS DE HAMBURGUESAS")
    print("=" * 50)
    
   # Lista de métodos de entrega
    metodos_entrega = ["mostrador", "retiro", "delivery", "moto"]
    
    # Recorrer la lista y crear/entregar cada hamburguesa
    for metodo in metodos_entrega:
        hamburguesa = Hamburguesa(metodo)
        hamburguesa.entregar()