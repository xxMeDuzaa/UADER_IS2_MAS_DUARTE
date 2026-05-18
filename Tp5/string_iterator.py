# string_iterator.py
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any

class StringIterator(Iterator):
    """
    Iterador concreto para recorrer una cadena carácter por carácter.
    Soporta dirección directa (forward) y reversa (reverse).
    """

    def __init__(self, collection: StringCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        # Posición inicial: 0 para directo, último índice para reverso
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self) -> str:
        """
        Retorna el siguiente carácter según la dirección.
        Lanza StopIteration cuando no hay más elementos.
        """
        if self._reverse:
            if self._position < 0:
                raise StopIteration()
            value = self._collection[self._position]
            self._position -= 1
        else:
            if self._position >= len(self._collection):
                raise StopIteration()
            value = self._collection[self._position]
            self._position += 1
        return value


class StringCollection(Iterable):
    """
    Colección concreta que almacena una cadena de caracteres.
    Proporciona métodos para obtener iteradores en ambas direcciones.
    """

    def __init__(self, text: str = "") -> None:
        self._text = text   # Almacenamos la cadena original

    def __len__(self) -> int:
        return len(self._text)

    def __getitem__(self, index: int) -> str:
        """Permite acceder a un carácter por índice (soporta índices negativos)."""
        return self._text[index]

    def __iter__(self) -> StringIterator:
        """Retorna un iterador en sentido directo (por defecto)."""
        return StringIterator(self, reverse=False)

    def get_reverse_iterator(self) -> StringIterator:
        """Retorna un iterador en sentido reverso."""
        return StringIterator(self, reverse=True)

    def add_text(self, extra: str) -> None:
        """Permite añadir más caracteres a la cadena (opcional)."""
        self._text += extra


if __name__ == "__main__":
    # Ejemplo de uso
    cadena = StringCollection("Hola Mundo")

    print("Recorrido directo:")
    for caracter in cadena:
        print(caracter, end=" ")   # H o l a   M u n d o
    print("\n")

    print("Recorrido reverso:")
    for caracter in cadena.get_reverse_iterator():
        print(caracter, end=" ")   # o d n u M   a l o H
    print()