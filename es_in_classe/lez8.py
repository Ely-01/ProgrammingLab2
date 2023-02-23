class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')


class IncrementModel(Model):

    def predict(self, data):
        if type(data) is not list:
            raise TypeError
        t = 0
        somma = 0
        for item in data:
            if t>0:
                incremento = item - data[t-1]
                #item = data[t]
                somma = somma + incremento
            t += 1
        media_incrementi = somma/(len(data)-1)

        previsione = data[-1] + media_incrementi
        return previsione

lista_test = 'ciao'
increment_model = IncrementModel()
print(increment_model.predict(lista_test))

        
              
        