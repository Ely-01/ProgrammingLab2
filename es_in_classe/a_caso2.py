# Funzione somma
def somma(a,b):
    return a+b
# Testing
if not somma(1,21) == 2:
    raise Exception('Test 1+1 non passato')

if not somma(1.5,2.5) == 4:
    raise Exception('Test 1.5+2.5 non passato')