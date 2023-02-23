try:
    my_var = float(my_var)
except ValueError:
    print('Non posso convertire "my_var" a valore numerico!')
    print('Ho avuto un errore VALORE. "my_var" valeva "{}".'.format(my_var))
except TypeError:
    print('Non posso convertire "my_var" a valore numerico!')
    print('Ho avuto un errore TIPO. "my_var" valeva "{}".'.format(my_var))
except Exception:
    print('Non posso convertire "my_var" a valore numerico!')
    print('Ho avuto un errore generico: "{}".'.format(Exception))

    
    