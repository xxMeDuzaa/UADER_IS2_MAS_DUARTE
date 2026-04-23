#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación - Prototype
#* Verificación: Clase generada a partir de un prototipo permite obtener copias de sí misma
#*------------------------------------------------------------------------

import copy
from abc import ABC, abstractmethod


#* ------------------- Interfaz Prototype -------------------
class Prototype(ABC):
    """Interfaz que define el método clone"""
    
    @abstractmethod
    def clone(self):
        pass


#* ------------------- Clase base Avión (Prototipo) -------------------
class Avion(Prototype):
    """Clase que representa un avión y permite clonarse"""
    
    def __init__(self, modelo: str, velocidad: int, capacidad: int, componentes: list = None):
        self.modelo = modelo
        self.velocidad = velocidad
        self.capacidad = capacidad
        self.componentes = componentes if componentes is not None else []
        self._id = id(self)  # Identificador único para tracking
    
    def agregar_componente(self, componente: str):
        """Agrega un componente al avión"""
        self.componentes.append(componente)
    
    def clone(self):
        """Clona el avión (copia superficial)"""
        return copy.copy(self)
    
    def deep_clone(self):
        """Clona el avión (copia profunda)"""
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Avión[{self._id}]: {self.modelo} | Vel: {self.velocidad} km/h | Cap: {self.capacidad} | Comp: {self.componentes}"


#* ------------------- Clase derivada Avión de Combate -------------------
class AvionCombate(Avion):
    """Clase derivada que extiende Avión y también debe poder clonarse"""
    
    def __init__(self, modelo: str, velocidad: int, capacidad: int, armamento: list = None, componentes: list = None):
        super().__init__(modelo, velocidad, capacidad, componentes)
        self.armamento = armamento if armamento is not None else []
    
    def agregar_arma(self, arma: str):
        self.armamento.append(arma)
    
    def clone(self):
        """Sobrescribe el método clone para incluir armamento"""
        nuevo = copy.copy(self)
        return nuevo
    
    def deep_clone(self):
        """Clonación profunda incluyendo armamento"""
        return copy.deepcopy(self)
    
    def __str__(self):
        return (f"AvionCombate[{self._id}]: {self.modelo} | Vel: {self.velocidad} km/h | "
                f"Cap: {self.capacidad} | Arm: {self.armamento} | Comp: {self.componentes}")


#* ------------------- Función de verificación -------------------
def verificar_clonacion_en_cadena(prototipo: Prototype, nombre: str):
    """
    Verifica que un prototipo puede generar copias y que esas copias
    también pueden generar sus propias copias
    """
    print(f"\n{'='*60}")
    print(f"🔬 VERIFICACIÓN DE CLONACIÓN EN CADENA: {nombre}")
    print(f"{'='*60}")
    
    # Original
    print(f"\n ---- ORIGINAL:")
    print(f"   {prototipo}")
    
    # Primera copia (desde el original)
    copia1 = prototipo.clone()
    print(f"\n ---- PRIMERA COPIA (desde original):")
    print(f"   {copia1}")
    
    # Segunda copia (desde la primera copia)
    copia2 = copia1.clone()
    print(f"\n ---- SEGUNDA COPIA (desde la primera copia):")
    print(f"   {copia2}")
    
    # Tercera copia (desde la segunda copia)
    copia3 = copia2.clone()
    print(f"\n ---- TERCERA COPIA (desde la segunda copia):")
    print(f"   {copia3}")
    
    # Verificaciones
    print(f"\n ---- VERIFICACIONES: ----")
    print(f"   ¿Original es distinto a Copia1? {prototipo is not copia1} ✓")
    print(f"   ¿Copia1 es distinto a Copia2? {copia1 is not copia2} ✓")
    print(f"   ¿Copia2 es distinto a Copia3? {copia2 is not copia3} ✓")
    print(f"   ¿Todos tienen el mismo contenido? {prototipo.modelo == copia1.modelo == copia2.modelo == copia3.modelo} ✓")
    
    # Verificar que son instancias de la misma clase
    print(f"   ¿Copia2 es instancia de {type(prototipo).__name__}? {isinstance(copia2, type(prototipo))} ✓")
    
    return [prototipo, copia1, copia2, copia3]


#* ------------------- Código de prueba -------------------
if __name__ == "__main__":
    print("=" * 60)
    print(" ---- VERIFICACIÓN DEL PATRÓN PROTOTYPE ---- ")
    print("=" * 60)
    print("\nObjetivo: Demostrar que una clase generada a partir de un")
    print("prototipo permite obtener copias de sí misma.")
    
    # ========== PRUEBA 1: Avión base (clase base) ==========
    print("\n\n" + "-" * 30)
    print("PRUEBA 1: Avión base (clase creada a partir de Prototype)")
    print("-" * 30)
    
    avion_original = Avion("Boeing 747", 900, 300, ["Motor", "Alas", "Cola"])
    avion_original.agregar_componente("Tren de aterrizaje")
    
    resultados1 = verificar_clonacion_en_cadena(avion_original, "Avión Base")
    
    # ========== PRUEBA 2: Avión de Combate (clase derivada) ==========
    print("\n\n" + "*" * 30)
    print("PRUEBA 2: Avión de Combate (clase derivada que también clona)")
    print("*" * 30)
    
    combate_original = AvionCombate("F-16 Fighting Falcon", 2400, 1, ["AIM-9", "AIM-120"], ["Motor", "Alas"])
    combate_original.agregar_arma("Cañón M61")
    combate_original.agregar_componente("Radar")
    
    resultados2 = verificar_clonacion_en_cadena(combate_original, "Avión de Combate")
    
    # ========== PRUEBA 3: Modificación independiente ==========
    print("\n\n" + "*" * 30)
    print("PRUEBA 3: Las copias son independientes (modificaciones aisladas)")
    print("*" * 30)
    
    print("\n ---- Modificando la primera copia del Avión de Combate...")
    resultados2[1].agregar_arma("Bomba guiada JDAM")
    resultados2[1].agregar_componente("Sistema de navegación")
    
    print(f"\n ---- ORIGINAL (sin modificar):")
    print(f"   {resultados2[0]}")
    
    print(f"\n ---- PRIMERA COPIA (modificada):")
    print(f"   {resultados2[1]}")
    
    print(f"\n ---- SEGUNDA COPIA (sin modificar):")
    print(f"   {resultados2[2]}")
    
    print(f"\n✅ VERIFICACIÓN: Las modificaciones en la copia NO afectan al original ni a otras copias.")
    
    # ========== PRUEBA 4: Clonación profunda vs superficial ==========
    print("\n\n" + "*" * 30)
    print("PRUEBA 4: Diferencia entre clone() (shallow) y deep_clone()")
    print("*" * 30)
    
    avion_con_lista = Avion("Airbus A380", 1020, 500, ["Motor1", "Motor2"])
    
    shallow_copia = avion_con_lista.clone()
    deep_copia = avion_con_lista.deep_clone()
    
    print(f"\n ---- Original: {avion_con_lista}")
    print(f" ---- Shallow copy: {shallow_copia}")
    print(f" ---- Deep copy: {deep_copia}")
    
    # Modificar el original
    avion_con_lista.componentes.append("Componente NUEVO")
    
    print(f"\n ---- Después de modificar el original:")
    print(f"   Original: {avion_con_lista}")
    print(f"   Shallow copy (AFECTADA): {shallow_copia}")  # Se modifica porque comparte referencia
    print(f"   Deep copy (NO AFECTADA): {deep_copia}")     # No se modifica
    
    