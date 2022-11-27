import random
countries = ['col','mex','bol', 'pe']

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

result = {country : population for (country, population) in population_v2.items() if population > 50}
print(result)

text = 'Hola, soy Carlos'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)

'''
        Mutable Ordenada Indexin Duplicar
List       1       1        1        1
Tuple      0       1        1        1
Set        1       0        0        0
'''