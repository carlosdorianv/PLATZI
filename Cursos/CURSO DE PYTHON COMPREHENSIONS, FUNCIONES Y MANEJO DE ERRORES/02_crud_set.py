set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('pe' in set_countries)
print('col' in set_countries)

set_countries.add('pe')
size = len(set_countries)
print(size)

#update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

#remove
set_countries.remove('col')
print(set_countries)

set_countries.discard('colo')

set_countries.clear()
print(set_countries)
