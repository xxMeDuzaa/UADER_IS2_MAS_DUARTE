
import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo con capacidad para 4 estados
#*-------------------------------------------------------------------
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    def __init__(self):
        self.mementos = []          # Almacena hasta 4 mementos
        self.max_states = 4

    def save(self, writer):
        """Guarda el estado actual, manteniendo como máximo 4 estados."""
        memento = writer.save()
        self.mementos.append(memento)
        if len(self.mementos) > self.max_states:
            self.mementos.pop(0)   # Elimina el más antiguo

    def undo(self, writer, steps=0):
        """
        Restaura un estado anterior.
        steps = 0 -> restaura el inmediato anterior (último guardado).
        steps = 1 -> restaura el anterior al último, etc.
        """
        if not self.mementos:
            print("No hay estados guardados para deshacer.")
            return

        # Calcular índice: el último es len-1, queremos ir hacia atrás steps+1
        # Ejemplo: steps=0 -> índice len-2 (el anterior al último)
        idx = len(self.mementos) - 2 - steps
        if idx < 0:
            print(f"No hay suficientes estados para deshacer {steps} pasos.")
            return

        memento = self.mementos[idx]
        writer.undo(memento)
        # Eliminar todos los estados posteriores al restaurado (incluyendo el actual)
        self.mementos = self.mementos[:idx+1]


if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior (hasta 4 estados)")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva (1)")
    writer.write("Clase de IS2 en UADER\n")
    caretaker.save(writer)
    print(writer.content)

    print("Se graba información adicional (2)")
    writer.write("Material adicional de la clase de patrones\n")
    caretaker.save(writer)
    print(writer.content)

    print("Se graba información adicional II (3)")
    writer.write("Material adicional de la clase de patrones II\n")
    caretaker.save(writer)
    print(writer.content)

    print("Se graba información adicional III (4)")
    writer.write("Material adicional de la clase de patrones III\n")
    caretaker.save(writer)
    print(writer.content)

    print("Se graba información adicional IV (5) - supera los 4, se descarta el primero")
    writer.write("Ultimo estado\n")
    caretaker.save(writer)
    print(writer.content)

    print("\n--- Prueba de deshacer ---")
    print("Deshacer 0 (inmediato anterior):")
    caretaker.undo(writer, steps=0)
    print(writer.content)

    print("\nDeshacer 1 (anterior al anterior):")
    caretaker.undo(writer, steps=1)
    print(writer.content)

    print("\nIntentar deshacer 3 (no hay tantos):")
    caretaker.undo(writer, steps=3)

    print("\nMostrar estado actual tras intento fallido:")
    print(writer.content)