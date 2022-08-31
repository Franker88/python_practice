#Assert sirve para hacer una afirmación directa, de lo contrario imprimir un error indicado

def palindrome(string):
  assert len(string) > 0, "No puede ingresarse una cadena vacia"
  return string == string[::-1]

print(palindrome(""))