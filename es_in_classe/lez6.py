

#Definisco la classe CSVFile
class CSVFile():
    
    #Definisco l'attributo names
    def __init__(self, name):
        self.name = name
        
    #Definisco self
    def get_data(self):
        pass
    
#Creo la sottoclasse
class NumericalCSVFile(CSVFile):
        
    #Definisco la funzione get data
    def get_data(self):
            
        #Provo se il file esiste o meno
        try:
                
            #Apro il file
            file = open(self.name, 'r')
                
            #Inizializzo una variabile flag
            vuoto = True
                
            #Creo una lista
            values = []
                
            #Leggo linea per line
            for line in file:
                    
                #Diviso gli elementi sulla virgola
                elements = line.split(',')
                elements[1]=elements[1].replace('\n', '')

             #Controllo se l'elemento 0 è diverso da date
                if elements[0]!='Date': 
                        
         #Attribuisco a value gli elementi delle colonna 1
                    value = elements[1]
#Provo se gli elementi della colonna 1 si possono convertire in float
                    try:
                        value=float(value)
                        values.append(value)        
                        vuoto = False
                    
                        #stampo i valori
                        print(value) 

#Se non si possono convertire stampo l'errore e vado avanti                            
                    except ValueError or TypeError as e:
                        print('Errore -> {}'.format(e))   

#Controllo la mia variabile flag e decido cosa returnare    
            if vuoto == False:
                return values
            else:
                return None
                
        except Exception as e:
            print("Errore -> {}".format(e))
   
my_file = NumericalCSVFile('shampoo_sales_error.csv')
my_file.get_data()

#Definisco la classe CSVFile
class CSVFile():
    
    #Definisco l'attributo names
    def __init__(self, name):
        self.name = name
        
    #Definisco self
    def get_data(self):
        pass
    
#Creo la sottoclasse
class NumericalCSVFile(CSVFile):
        
    #Definisco la funzione get data
    def get_data(self):
            
        #Provo se il file esiste o meno
        try:
                
            #Apro il file
            file = open(self.name, 'r')
                
            #Inizializzo una variabile flag
            vuoto = True
                
            #Creo una lista
            values = []
                
            #Leggo linea per line
            for line in file:
                    
                #Diviso gli elementi sulla virgola
                elements = line.split(',')
                elements[1]=elements[1].replace('\n', '')

         #Controllo se l'elemento 0 è diverso da date
                if elements[0]!='Date': 
                        
        #Attribuisco a value gli elementi delle colonna 1
                    value = elements[1]
                        
 #Provo se gli elementi della colonna 1 si possono convertire in float
                    try:
                        value=float(value)
                        values.append(value)        
                        vuoto = False
                    
                        #stampo i valori
                        print(value) 

#Se non si possono convertire stampo l'errore e vado avanti                            
                    except ValueError or TypeError as e:
                        print('Errore -> {}'.format(e))   

#Controllo la mia variabile flag e decido cosa returnare    
            if vuoto == False:
                return values
            else:
                return None
                
        except Exception as e:
            print("Errore -> {}".format(e))
   
my_file = NumericalCSVFile('shampoo_sales_error.csv')
my_file.get_data()