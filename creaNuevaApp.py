import os

def crear_nueva_app(nombre_app):
  """Crea una nueva aplicación con la estructura especificada.

  Args:
    nombre_app: El nombre de la carpeta de la nueva aplicación.
  """

  # Ruta completa a la nueva carpeta
  ruta_app = os.path.join("sulkusers_data", nombre_app)

  # Crear la carpeta si no existe
  os.makedirs(ruta_app, exist_ok=True)

 # Verificar si los archivos ya existen
  ruta_data = os.path.join(ruta_app, "data.py")
  ruta_novelty = os.path.join(ruta_app, "novelty.py")

  if not os.path.exists(ruta_data):
    # Crear el archivo data.py si no existe
    with open(ruta_data, "w") as f:
      f.write("[('ella', '12345')]")

  if not os.path.exists(ruta_novelty):
    # Crear el archivo novelty.py si no existe
    with open(ruta_novelty, "w") as f:
      f.write("[('ella', 'user')]")

# Ejemplo de uso:
crear_nueva_app("t2i-dev")