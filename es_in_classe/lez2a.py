def sum_list(lista):
    if len(lista)==0:
        return None
    else:
        return sum(lista)

lista = []  #lista numeri
print("Risultato {}".format(sum_list(lista)))