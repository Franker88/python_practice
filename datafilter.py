DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
  #solo nombres de python devs
  all_py_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
  #Trabajadores de platzi
  all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
  #Adultos
  all_adults = list(filter(lambda worker: worker["age"] > 18,DATA))
  all_adults = list(map(lambda worker: worker["name"],all_adults))
  #Old true or false
  old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

  for worker in all_py_devs:
    print(worker)

  print("-----------")

  for worker in all_platzi_workers:
    print(worker)

  print("-----------")

  for worker in all_adults:
    print(worker)

  for worker in old_people:
    print(worker)
run()