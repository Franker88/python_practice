def run():
  #Listas normales
  pow_list = []
  for i in range(1,101):
    if i%3 != 0:
      pow_list.append(i ** 2)
    
  
  for value in pow_list:
    print(value)

  print(pow_list)

  #List Comprehension
  #Estructura: = [element(s) for element in iterable if condition]
  squares = [i**2 for i in range(1,101) if i % 3 != 0]
  print(squares)
run()