#r para leer
#w para escribir (sobre escribir)
#a para escribir (añadir)

def read():
  numbers = []
  with open("./archivos/number.txt","r",encoding="utf-8") as f:
    for line in f:
      numbers.append(int(line))
  print(numbers)

def write():
  names = ["Carlos","Luis","German","Diego","Rocío"]
  with open("./archivos/names.txt","w",encoding="utf-8") as f:
    for name in names:
      f.write(name)
      f.write("\n")

def run():
  read()

if __name__ == "__main__":
  run()