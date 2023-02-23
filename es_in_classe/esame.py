import os

def ExamException(Exception):
    pass

# Creo una classe CSVFile per rappresentare un file CSV
class CSVTimeSeriesFile:
# Il metodo __init__ inizializza un'istanza di CSVFile con il nome del file
    def __init__(self, name):
        self.name = name
    # Metodo per leggere il file CSV
    def read_csv(self):
    # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))

      # Prendo ogni riga nel file e la memorizzo nell'elenco dei dati
        data = [row for row in my_file]
            # Resturno l'elenco dei dati: data
        return data

    def get_data(self):
        data = self.read_csv()
        if data:
            time_series = []
            #Escludo la prima linea, intestazione
            for row in data[1:]: 
                try:
                    epoch = int(row[0])
                except (ValueError, TypeError):
                    print("Errore: il valore di epoch '{row[0]}' non è un intero")
                    continue
                if epoch is None:
                    print("Errore: il valore di epoch è None")
                    continue
                try:
                    temperature = float(row[1])
                except (ValueError, TypeError):
                    print("Errore: il valore di temperatura '{row[1]}' non è un float")
                    continue
                if temperature is None:
                    print(f"Errore: il valore di temperatura è None")
                    continue
                time_series.append([epoch, temperature])
            return time_series
        return []
# Funzione per calcolare la differenza massima giornaliera
def compute_daily_max_difference(time_series: List[List[int]]) -> List[float]:
    if not time_series:
        return []
    daily_max_differences = []
    day = {}
    for timestamp, temperature in time_series:
        if temperature is None:
            continue
        date = timestamp // 86400 # un giorno ha 86400 secondi
        if date not in day:
            day[date] = (temperature, temperature)
        else:
            day[date] = (min(day[date][0], temperature), max(day[date][1], temperature))
    for (min_temp, max_temp) in day.values():
        if min_temp is None or max_temp is None:
            continue
        daily_max_differences.append(max_temp - min_temp)
    return daily_max_differences
# Creo un'istanza di CSVTimeSeriesFile
time_series_file = CSVTimeSeriesFile(name='data.csv')
# Ottengo i dati dal file
time_series = time_series_file.get_data()