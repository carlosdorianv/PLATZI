set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4}
print(set_numbers)

print('pe' in set_countries)


def sum(a, b):
  result = a+b
  print(result)
  return result

sum_set = {}

sum_set.add(sum(1,2))
print(sum_set)
