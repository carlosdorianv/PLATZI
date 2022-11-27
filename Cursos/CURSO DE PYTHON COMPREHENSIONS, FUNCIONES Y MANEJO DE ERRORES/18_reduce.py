import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = functools.reduce(accum, numbers)

'''
             iteration     counter    item    return
                  1            0        1        1
                  2            1        2        3
                  3            3        3        6
                  4            6        4        10
            
'''
print(result)