

def run():
  #Forma normal
  pow_dict = {}
  for i in range(1,101):
    pow_dict[i] = i**3  

  print(pow_dict)

  #Dict Comprehension
  #Misma sintaxis (llave:valor | bucle for | condicional)
  cubics = {
    i:i**3 for i in range(1,101) if i%3 != 0
  }

  print(cubics)
run()

