#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
getJason.py - Recuperador de tokens desde sitedata.json

Copyright UADER-FCyT-IS2 © 2024 - Todos los derechos reservados.

Este programa lee el archivo sitedata.json (formato JSON) y devuelve el valor
asociado a una clave especificada como argumento (por defecto 'token1').
Implementa un patrón Singleton para la nueva versión y utiliza Branching by
Abstraction para permitir la convergencia entre la versión original procedural
y la versión refactorizada orientada a objetos.

Uso:
    python getJason.py [clave]
    python getJason.py -v

Opciones:
    -v          Muestra la versión del programa y termina.
    clave       Opcional: nombre de la clave a recuperar (por defecto 'token1').

Variable de entorno:
    USE_LEGACY=1    Usa la implementación legacy (procedural) en lugar de la nueva.
"""

import json
import sys
import os
from abc import ABC, abstractmethod

# ============================================================================
# Carátula y copyright (punto e)
# ============================================================================
__author__ = "UADER FCyT - IS2"
__copyright__ = "Copyright UADER-FCyT-IS2 © 2024 - Todos los derechos reservados"
__version__ = "1.1"
__status__ = "Production"

# ============================================================================
# Abstracción para Branching by Abstraction (punto d)
# ============================================================================
class TokenReaderInterface(ABC):
    """Interfaz abstracta para mitigar cambios por abstracción."""
    
    @abstractmethod
    def get_token(self, key: str) -> str:
        """Método abstracto para recuperar tokens."""

# ----------------------------------------------------------------------------
# Implementación Legacy (original procedural)
# ----------------------------------------------------------------------------
class LegacyTokenReader(TokenReaderInterface):
    """
    Versión original procedural (similar al código antes de la refactoría).
    No usa Singleton; lee el archivo cada vez que se pide un token.
    """
    def __init__(self, filename: str = 'sitedata.json'):
        self.filename = filename

    def _load_json_file(self) -> dict:
        """Carga y parsea el JSON, manejando errores de forma controlada."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error controlado: No se encontró el archivo '{self.filename}'.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error controlado: El archivo '{self.filename}' no tiene formato JSON válido.")
            sys.exit(1)
        except PermissionError:
            print(f"Error controlado: Permisos insuficientes para leer '{self.filename}'.")
            sys.exit(1)

    def get_token(self, key: str) -> str:
        """Lee el archivo cada vez y devuelve el token o error controlado."""
        data = self._load_json_file()
        if key in data:
            return str(data[key])
        print(f"Error controlado: La clave '{key}' no existe en el archivo JSON.")
        sys.exit(1)

# ----------------------------------------------------------------------------
# Implementación refactorizada (Singleton)
# ----------------------------------------------------------------------------
class JsonTokenReader(TokenReaderInterface):
    """
    Clase Singleton que gestiona la lectura de tokens desde un archivo JSON.
    Garantiza una única instancia en toda la ejecución del sistema.
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filename: str = 'sitedata.json'):
        if self._initialized:
            return
        self.filename = filename
        self.data_dict = self._load_json_file()
        self._initialized = True

    def _load_json_file(self) -> dict:
        """Carga de manera interna el archivo JSON, con manejo controlado de errores."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as myfile:
                return json.loads(myfile.read())
        except FileNotFoundError:
            print(f"Error controlado: No se encontró el archivo '{self.filename}'.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error controlado: El archivo '{self.filename}' no tiene formato JSON válido.")
            sys.exit(1)
        except PermissionError:
            print(f"Error controlado: Permisos insuficientes para leer '{self.filename}'.")
            sys.exit(1)

    def get_token(self, key: str) -> str:
        """Devuelve el valor de la clave especificada."""
        if key in self.data_dict:
            return str(self.data_dict[key])
        print(f"Error controlado: La clave '{key}' no existe en el archivo JSON.")
        sys.exit(1)

# ============================================================================
# Funciones auxiliares
# ============================================================================
def print_version():
    """Imprime la versión actual del programa (punto g)."""
    print(f"getJason.py versión {__version__}")
    sys.exit(0)

def validate_and_parse_arguments():
    """
    Valida rigurosamente los argumentos de la línea de comandos (puntos c y f).
    Maneja la bandera de versión y límites de parámetros.
    """
    arguments = sys.argv[1:]

    # Control de bandera de versión
    if "-v" in arguments:
        print_version()

    # Si se pasan más argumentos de los esperados
    if len(arguments) > 1:
        print("Error controlado: Demasiados argumentos de ejecución.")
        print("Uso: python getJason.py [clave]  o  python getJason.py -v")
        sys.exit(1)

    # Retorna la clave por defecto 'token1' si no se provee argumento
    return arguments[0] if len(arguments) == 1 else 'token1'

def select_token_reader() -> TokenReaderInterface:
    """
    Branching by Abstraction (punto d).
    Decide qué implementación usar según la variable de entorno USE_LEGACY.
    """
    use_legacy = os.environ.get('USE_LEGACY', '0') == '1'
    if use_legacy:
        # Se puede imprimir un mensaje en modo debug si se desea
        # print("Usando implementación Legacy (procedural)")
        return LegacyTokenReader()
    else:
        # print("Usando implementación Singleton refactorizada")
        return JsonTokenReader()

# ============================================================================
# Función principal
# ============================================================================
def main():
    """Punto de entrada principal de la aplicación refactorizada."""
    # Validación robusta de argumentos de ejecución
    json_key = validate_and_parse_arguments()

    # Selección dinámica de implementación (Branching by Abstraction)
    reader: TokenReaderInterface = select_token_reader()

    # Obtener el token (si hay error, el programa ya habrá terminado con sys.exit)
    token_value = reader.get_token(json_key)

    # Salida estándar exitosa
    print(token_value)

if __name__ == '__main__':
    main()