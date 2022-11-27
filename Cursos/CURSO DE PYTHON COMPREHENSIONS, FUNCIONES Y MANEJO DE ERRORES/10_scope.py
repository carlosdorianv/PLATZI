price = 100  #Global

def increment():
  price = 200   #Local
  price = price + 10
  print(price)
  return price

print(price)
price_2 = increment()
print(price_2)
