from pathlib import Path           
#importo la CLASSE PATH 

class ExamException(Exception):    #classe eccezioni        
    pass    

class CSVTimeSeriesFile():           
#classeCSV#
______________________________________________________________        
def __init__(self, name = None):                
    self.name = name
#______________________________________________________________    

def file_exists(self):    #uso la CLASSE PATH    
    #questa funzione mi serve per capire se un file esiste in una cartella            
    CSVpath = Path(self.name)        
    if(CSVpath.is_file() == True):            
        return True        
    else:            
        return False
#______________________________________________________________        
def get_data(self):        
    if(self.name is None):  
        #se hanno istanziato la classe senza file            
        raise ExamException("You forgot to type the name of the file!")                
    try:            
        self.name = str(self.name)         
    except TypeError:              
        #se il nome file non va bene            
        raise ExamException("It seems that the name of the file is not a valid file name, please check again.")                           
    
    if(self.file_exists()==False):        
        #se il file non esiste            
        raise ExamException("No such file found within this directory.")                                                
    try:                                                  
        CSVopen = open(self.name, "r")                    
        CSVopen.readline()        
    except Exception as e: 
        #se il file esiste ma non si apre            
        raise ExamException(f"Couldn't open file because of following error: {e}.")        
    
    return_list = []        
    #lista coi dati puliti da dare alla funzione esterna                  
    
    prev_epoch = None                
    
    for line in CSVopen :                        
        entries = line.split(",")                        
        try:                
            entries[0] = int(float(entries[0]))         
            #conversione elementi a SX.                
            entries[1] = float(entries[1])              
            #conversione elementi a DX.                
            prov_list = [entries[0], entries[1]] 
            #elementi della lista finale                
            return_list.append(prov_list)                
            if ( entries[0] < prev_epoch):                    
                raise ExamException("La lista potrebbe non essere correttamente ordinata!")                    
            if (entries[0] == prev_epoch):                    
                raise ExamException("Warning: this list contains duplicates!")            
            except TypeError:  #questo mi serviva molto per l'intestazione del CSV                continue                        
            except:            #eccezione generica                
                continue            
            prev_epoch = entries[0]        
        return return_list   
######################################################################################################################################
def compute_daily_max_difference (time_series):    
    return_list = []    #qui metto tutta la roba di Marzo 2k19    
    i = 0               #indice        
    epoch = time_series[i][0]                    #epoch iniziale    
    day_start_epoch = epoch - (epoch % 86400)    #inizio primo giorno    
    next_day = day_start_epoch + 86400           #second day        
    
    while(i < len(time_series)):                 #per tutta la lista        
        daily_recs = []                  #valori giornalieri qui in questa lista        
        temperature = time_series[i][1]          
        daily_recs.append(temperature)   #aggiungo temperatura primo giorno                
        for j in range  (i+1, len(time_series)):    #dal successivo in poi            
            epoch = time_series[j][0]               #epoch corrente aggiornato            
            temperature = time_series[j][1]         #temp. aggiornata                            
            
            if (epoch < next_day):             #se siam nello stesso giorno di prima                
                daily_recs.append(temperature) #aggiungo temperatura            
            else:                
                break                          #altrimenti passa a valutare un giorno successivo                        
        
        i = i+len(daily_recs)       #riprendo dal giorno successivo        
        day_start_epoch = epoch - (epoch % 86400)    #aggiorno tutto        
        next_day = day_start_epoch + 86400                            
        if (len(daily_recs) == 1):  #se ho solo una misurazione per quel giorno            
            daily_excursion = None                
        else:                       #se ho più temperature per un giorno            
            daily_max = max(daily_recs)            
            daily_min = min(daily_recs)            
            daily_excursion = daily_max - daily_min                                                    
                
        return_list.append(daily_excursion)  #metto l'escursione        

return return_list
###############################################################################################    

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print("Here's the list with all the valid data from the CSV file:")
print(time_series)
print("__________________________________________________")
print("Here's the list of March 2019 temperature excursion measurements:")
print(compute_daily_max_difference(time_series)