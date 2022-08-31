def palindrome(string):
  try:
    if len(string) == 0:
      raise ValueError("No se aceptan cadenas vacias") #Un tipo de error variado según el if
    return string == string[::1]
  except ValueError as ve: #Trae el value error del raise para imprimirlo
    print(ve)
    return False

try:
  print(palindrome("ana"))
except TypeError: 
  print("Solo se pueden ingresar strings")
finally: #No suele usarse, sirve para ejecutar algo al final sin importar las cosas
  print("Ejecutado correctamente")
