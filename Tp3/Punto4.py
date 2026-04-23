#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación - Factory Method
#* Extendido para construir FACTURAS 
#*------------------------------------------------------------------------

class Factura:
    """Clase que genera facturas según condición impositiva"""
    
    def __init__(self, importe: float, condicion_impositiva: str):
        self.importe = importe
        self.condicion = condicion_impositiva.lower()
    
    def generar(self) -> str:
        """Genera y retorna la factura formateada"""
        
        if self.condicion == "responsable":
            iva = 21
            total = self.importe + (self.importe * iva / 100)
            return (f"FACTURA - IVA RESPONSABLE\n"
                   f"   Importe neto: ${self.importe:.2f}\n"
                   f"   IVA {iva}%: ${self.importe * iva / 100:.2f}\n"
                   f"   TOTAL: ${total:.2f}")
        
        elif self.condicion == "no_inscripto":
            return (f"FACTURA - IVA NO INSCRIPTO\n"
                   f"   Importe total: ${self.importe:.2f}\n"
                   f"   (No corresponde IVA)")
        
        elif self.condicion == "exento":
            return (f"FACTURA - IVA EXENTO\n"
                   f"   Importe total: ${self.importe:.2f}\n"
                   f"   (Exento de IVA)")
        
        else:
            return f"Condición impositiva '{self.condicion}' no válida"


#*------------------- Código de prueba -------------------
if __name__ == "__main__":
    print("=" * 50)
    print("SISTEMA DE FACTURACIÓN")
    print("=" * 50)
    print()
    
    # Lista de condiciones impositivas
    condiciones = ["responsable", "no_inscripto", "exento"]
    importe = 1000.00
    
    for condicion in condiciones:
        print(f"\n--- Cliente: {condicion.upper()} ---")
        factura = Factura(importe, condicion)
        print(factura.generar())
        print()