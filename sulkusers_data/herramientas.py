def separar_letras_numeros(cadena):
  """Separa las letras de los números en una cadena.

  Args:
    cadena: La cadena a separar.

  Returns:
    Una tupla con dos elementos:
      - El primer elemento es la parte de la cadena que contiene las letras.
      - El segundo elemento es la parte de la cadena que contiene los números.
  """

  # Extraemos los últimos 3 caracteres (los números)
  numeros = cadena[-3:]

  # Extraemos las letras (todo lo que va antes de los números)
  letras = cadena[:-3]

  return letras, numeros

def revolver_letras(nombre):
  """Revuelve las letras de un nombre según una secuencia fija de índices.

  Args:
    nombre: El nombre a revolver.

  Returns:
    Una cadena con las letras del nombre revueltas.
  """

  # Diccionario para asignar índices a las letras (ejemplo)
  indices_letras = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                  'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                  'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

  # Secuencia fija de índices para permutar (ejemplo)
  secuencia_permutacion = [2, 0, 1, 3]  # Puedes personalizar esta secuencia

  # Convertir el nombre a minúsculas y obtener los índices de las letras
  indices_nombre = [indices_letras[c] for c in nombre.lower()]

  # Permutar los índices según la secuencia
  indices_permutados = [indices_nombre[i] for i in secuencia_permutacion]

  # Convertir los índices permutados de vuelta a letras
  letras_permutadas = [list(indices_letras.keys())[i] for i in indices_permutados]

  # Unir las letras permutadas en una cadena
  nombre_revuelto = ''.join(letras_permutadas)

  return nombre_revuelto

def sumar_numeros_finales(nombre_usuario):
  """Suma los tres últimos dígitos de un nombre de usuario.

  Args:
    nombre_usuario: El nombre de usuario a procesar.

  Returns:
    La suma de los tres últimos dígitos.
  """

  # Extraemos los tres últimos dígitos
  digitos = nombre_usuario[-3:]

  # Convertimos los dígitos a números enteros y los sumamos
  suma = sum(int(digito) for digito in digitos)

  return suma

def escritor_tuplas(tupla, aplicacion, set):
  
  print(f"Nuevo set: {tupla} para la aplicación: {aplicacion}.")
  # Leer los datos existentes del archivo
  with open('sulkusers_data' + '/' + aplicacion + '/' + set + '.py', 'r') as f:
        datos_existentes = eval(f.read())
  # Insertar la nueva tupla al inicio de la lista
  datos_existentes.insert(0, tupla)
  # Escribir los datos actualizados en el archivo
  with open('sulkusers_data' + '/' + aplicacion + '/' + set + '.py', 'w') as f:
      f.write(str(datos_existentes))