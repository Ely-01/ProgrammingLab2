def sum_list(my_list):
  risultato = 0
  for item in my_list:
    risultato = risultato + item
  return risultato

my_list = []  #lista numeri
print("Risultato {}".format(sum_list(my_list)))
