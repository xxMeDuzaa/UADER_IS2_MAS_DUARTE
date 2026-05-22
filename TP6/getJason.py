import json
import sys

# Archivo fijo según documentación
jsonfile = 'sitedata.json'

# Clave: primer argumento (si existe), o 'token1' por defecto
jsonkey = sys.argv[1] if len(sys.argv) > 1 else 'token1'

try:
    with open(jsonfile, 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    print(str(obj[jsonkey]))
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {jsonfile}")
except KeyError:
    print(f"Error: La clave '{jsonkey}' no existe en el archivo JSON")
except Exception as e:
    print(f"Error inesperado: {e}")