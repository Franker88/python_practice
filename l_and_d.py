def run():
  my_list = [1, "Hello", True, 4.5]
  my_dict = {"firstname":"Carlos","lastname":"Franco","age":22}

  super_list = [
    {"firstname":"Luis","lastname":"Franco","age":38},
    {"firstname":"Jean","lastname":"Contretas","age":42},
    {"firstname":"Liskeyli","lastname":"Pena","age":27}
  ]

  super_dict = {
    "natural_nums":[1,2,3,4,5],
    "integer_nums":[-1,-2,0,1,2],
    "floating_nums":[1.1,2.2,3.3,4.4]
  }

  for key, value in super_dict.items():
    print(key,"-",value)

  for value in super_list:
    for keys, values in value.items():
      print(keys,"-",values)
  
run()
if __name__ == "__main__":
  run()
