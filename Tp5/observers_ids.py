# observer_ids.py
class Subject:
    def __init__(self):
        self._observers = []

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


class IDEmitter(Subject):
    def __init__(self, name=''):
        super().__init__()
        self.name = name
        self._current_id = None

    @property
    def current_id(self):
        return self._current_id

    @current_id.setter
    def current_id(self, value):
        self._current_id = value
        self.notify()


class IDObserver:
    def __init__(self, observer_id, name):
        self.observer_id = observer_id
        self.name = name

    def update(self, subject):
        if subject.current_id == self.observer_id:
            print(f"{self.name} (ID: {self.observer_id}) recibió su ID: {subject.current_id}")


class ObserverA(IDObserver):
    def __init__(self):
        super().__init__("ABCD", "ObserverA")

class ObserverB(IDObserver):
    def __init__(self):
        super().__init__("EFGH", "ObserverB")

class ObserverC(IDObserver):
    def __init__(self):
        super().__init__("IJKL", "ObserverC")

class ObserverD(IDObserver):
    def __init__(self):
        super().__init__("MNOP", "ObserverD")


if __name__ == "__main__":
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

    emitter = IDEmitter("ID Emisor")
    obsA = ObserverA()
    obsB = ObserverB()
    obsC = ObserverC()
    obsD = ObserverD()

    emitter.attach(obsA)
    emitter.attach(obsB)
    emitter.attach(obsC)
    emitter.attach(obsD)

    ids_to_emit = ["ABCD", "WXYZ", "EFGH", "0000", "IJKL", "PPPP", "MNOP", "ZZZZ"]

    print("Emisor comenzará a emitir IDs:\n")
    for idx, id_value in enumerate(ids_to_emit, 1):
        print(f"Emisión #{idx}: {id_value}")
        emitter.current_id = id_value
        print()