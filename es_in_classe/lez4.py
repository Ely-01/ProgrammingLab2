class CSVFile():
    def __init__(self, name):
        self.name = name

    def get_data(self):
        values = []
        dates = []
        final_list = []

        file = open(self.name, 'r')

        vuoto = True

        for line in file:
            elements = line.split(',')
            
            if elements[0]!='Date': 
                date = elements[0]
                value = elements[1]

                value=float(value)
                values.append(value)
                dates.append(date)

                final_list = [date, value]
                print(final_list)

                vuoto = False
            
        if vuoto == False:
            return final_list
        else:
            return None
    
#my_file = File('shampoo_sales.csv')
#my_file.get_data()