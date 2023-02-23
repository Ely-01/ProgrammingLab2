from datetime import date

# adatto Exception al mio programma


class ExamException(Exception):
    pass

# classe per leggere il file CSV


class CSVTimeSeriesFile():

    # definisco il metodo init che prende come argomento il nome del file
    def __init__(self, name=None):
        self.name = name

    # definisco il metodo get_data
    def get_data(self):

        # provo ad aprire il file
        try:
            my_file = open(self.name)
        # se non riesco ad aprirlo alzo un'eccezione
        except:
            raise ExamException("Il file non può essere aperto o non esiste.")

        # provo a leggere il file
        try:
            data_file = my_file.read()
        # se non riesco a leggerlo alzo un'eccezione
        except:
            raise ExamException("Il file non è leggibile.")

        # splitto le linee del file
        lines_data = data_file.split("\n")

        # creo una lista
        my_list = []
        today = date.today()

        # per ogni linea splitto rispetto alla virgola
        for line in lines_data:
            line_data = line.split(",")

            if len(line_data) >= 2:
                if "-" in line_data[0]:

                    data_ok = True

                    # divido la data in anno e mese per controllarli separatamente
                    year_str = line_data[0].split("-")[0]
                    month_str = line_data[0].split("-")[1]
                    

                    try:
                        # anno e mese devono essere interi
                        year = int(year_str)
                        month = int(month_str)

                        # mese non conforme
                        if month < 1 or month > 12:
                            data_ok = False

                        # anno non conforme
                        if year < 0:
                            data_ok = False
                        elif year > today.year:
                            data_ok = False
                        elif year == today.year and month > today.month:
                            data_ok = False

                    except:
                        data_ok = False

                    try:
                        # il numero dei passeggeri deve essere intero
                        number_passengers = int(line_data[1])

                        # numero passeggeri deve essere positivo
                        if number_passengers < 0:
                            data_ok = False

                    except:
                        data_ok = False

                    if data_ok == True:
                        # aggiungo alla mia lista solo gli elementi conformi
                        my_list.append([line_data[0], number_passengers])

        # controllo che la lista non sia vuota
        if len(my_list) > 1:
            control_date = my_list[0][0]
            # verifico che non ci siano duplicati o date non ordinate
            for line in my_list[1:]:
                if line[0] == control_date:
                    raise ExamException("Ho un duplicato!")

                if line[0] < control_date:
                    raise ExamException("Le date non sono ordinate!")

                control_date = line[0]

        return my_list


def detect_similar_monthly_variations(time_series, years):

    # controllo che i valori di years siano interi
    for item in years:
        if not isinstance(item, int):
            raise ExamException("La lista years non è valida.")

    if (years[0] + 1 != years[1]):
        raise ExamException("La lista years non è valida.")

    if(years[0] < 0 or years[1] < 0):
        raise ExamException("La lista years non è valida.")

    # inizializzo le due liste con tutti valori None
    year1 = []
    year2 = []

    for item in range(0, 12):
        year1.append(None)
        year2.append(None)

    # riempio le liste con i valori che sono presenti nel file(se ci sono)
    for item in time_series:
        year = int(item[0].split("-")[0])
        month = int(item[0].split("-")[1])
        if year == years[0]:
            year1[month - 1] = item[1]
        elif year == years[1]:
            year2[month - 1] = item[1]

    # controllo che ci sia almeno un dato per quell'anno
    year_is_present = False

    for item in range(0, 12):
        if not (year1[item] == None):
            year_is_present = True

    # altrimenti se non esiste l'anno nel File, lancio l'eccezione
    if year_is_present == False:
        raise ExamException("Anno non presente nel File")

    # controllo che ci sia almeno un dato per quell'anno
    year_is_present = False
    for item in range(0, 12):
        if not year2[item] == None:
            year_is_present = True

    # altrimenti se non esiste l'anno nel File, lancio l'eccezione
    if year_is_present == False:
        raise ExamException("Anno non presente nel File")

    # lista per contenere i True e False richiesti come output finale
    final_list = []
    for index in range(1, 12):
        # se un valore è None, considero False, altrimenti valuto la differenza
        if (year1[index] == None or year1[index - 1] == None):
            final_list.append(False)
        elif (year2[index] == None or year2[index - 1] == None):
            final_list.append(False)
        else:
            difference1 = year1[index] - year1[index - 1]
            difference2 = year2[index] - year2[index - 1]

            if (difference1 - difference2 <= 2
                    and difference1 - difference2 >= -2):
                final_list.append(True)
            else:
                final_list.append(False)

    return final_list

#prova = CSVTimeSeriesFile("data.csv")
#print(detect_similar_monthly_variations(prova.get_data(), [1949, 1950]))
