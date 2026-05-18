import os

#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

    def scan_memories(self):
        # Este método debe ser implementado por las subclases
        raise NotImplementedError

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def scan_memories(self):
        # Delega en el radio el barrido de memorias
        self.radio.scan_memories()

#*------- Implementa como barrer las estaciones de FM
class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def scan_memories(self):
        self.radio.scan_memories()

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:

    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate   # Inicialmente en FM

        # Memorias: cada una es un diccionario con banda y frecuencia
        self.memories = [
            {"banda": "AM", "frecuencia": "550", "etiqueta": "M1"},
            {"banda": "FM", "frecuencia": "98.5", "etiqueta": "M2"},
            {"banda": "AM", "frecuencia": "1600", "etiqueta": "M3"},
            {"banda": "FM", "frecuencia": "104.3", "etiqueta": "M4"}
        ]
        self.mem_pos = 0   # Índice de la memoria actual

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

    def scan_memories(self):
        """Recorre las memorias cíclicamente y cambia el estado según la banda de la memoria."""
        self.mem_pos = (self.mem_pos + 1) % len(self.memories)
        mem = self.memories[self.mem_pos]
        # Cambiar al estado correspondiente según la banda de la memoria
        if mem["banda"] == "AM":
            self.state = self.amstate
        else:
            self.state = self.fmstate
        print("Sintonizando... Memoria {}: {} {}".format(mem["etiqueta"], mem["frecuencia"], mem["banda"]))

#*---------------------

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    # Secuencia de acciones: 3 scans, toggle, 3 scans, luego 4 scans de memorias, y repetimos un ciclo
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3 + [radio.scan_memories] * 4
    actions *= 2   # Repetir la secuencia dos veces

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()