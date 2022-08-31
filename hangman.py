from random import random
import os

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")


clear()

def read():
  intro = []
  with open("./archivos/hangplantilla.txt","r",encoding="utf-8") as f:
    for line in f:
      intro.append(str(line))
  intro= ' '.join(intro)
  return intro

def search(lista,filllista,letter):
  bien=False
  for i in range(0,len(lista)):
    if lista[i]==letter:
      filllista[i]=letter
      bien=True
  return bien

def play():
  words = []
  with open("./archivos/words.txt","r",encoding="utf-8") as f:
    for line in f:
      words.append(line)

  selected = words[int((random()*(100*(len(words))/100)))]
  selected = list(selected)
  selected.pop()
  
  menu = read()
  filltheword = []
  for i in range(0,len(selected)):
    filltheword.append("_")
  
  tries = 10
  win = False
  while(tries > 0 and win == False ):
    acertado = ""
    clear()
    blankword = " ".join(filltheword)
    blankword = "Letras: "+blankword
    game = menu + blankword
    print(game)
    print(tries)
    letra = input("Inserte una letra: ")
    if letra.isnumeric() == True:
      print("Solo están permitidos carácteres de letras")
    else:
      acertado = search(selected, filltheword, letra)
      if acertado == False:
        tries -= 1
      else:
        print(filltheword==selected)
        if filltheword == selected:
          win = True
          clear()
          break
          
  if win==True:
    ganar = []
    with open("./archivos/win.txt","r",encoding="utf-8") as f:
      for line in f:
        ganar.append(line)
      ganar="".join(ganar)
    clear()
    print(ganar)
  else:
    perder = []
    with open("./archivos/lose.txt","r",encoding="utf-8") as f:
      for line in f:
        perder.append(line)
      perder="".join(perder)
    clear()
    print(perder)

def run():
  jugar = "si"
  while jugar!="no" or jugar!="NO" or jugar!="No" or jugar!="nO":
    #clear()
    jugar = input("¿Deseas jugar una nueva partida?: ")
    if jugar.isnumeric()==True:
      print("No es una opción valida")
    else:
      if jugar == "si" or jugar == "Si" or jugar == "SI" or jugar == "sI":
        play()
      elif jugar == "no" or jugar == "No" or jugar == "NO" or jugar == "nO":
        jugar == "no"
        break
      else:
        print("No es una opción valida")
  clear()
  print("Fin del juego")
    
if __name__ == "__main__":
  run()

