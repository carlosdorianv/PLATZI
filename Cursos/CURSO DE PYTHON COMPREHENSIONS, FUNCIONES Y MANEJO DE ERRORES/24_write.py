with open('./text.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('Estoy muy loco\n')
  file.write('otra linea\n')
  file.write(' mas linea\n')