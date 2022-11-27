def increment(x):
  return x + 1
def high_ord_func(x, func):
  return x + func(x)
result = high_ord_func(2,increment) 
print(result) 


high_ord_func_v2 = lambda x, func: x + func(x)
increment_v2 = lambda x: x + 1
result = high_ord_func_v2(2, increment_v2)
print (result)

result = high_ord_func_v2(2, lambda x: x + 1)
print(result)