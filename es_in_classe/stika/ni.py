from contextlib import ExitStack
from logging.config import valid_ident
from typing_extensions import dataclass_transform

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    #Costruttore per il file name
    def _init_(self, name = None):
        self.name = name

    def get_data(self):

        #raise file name non è una stringa
        if not isinstance(self.name, str):
            raise ExamException("Wrong file name")
        
        #raise file illegibile
        try:
            data_file = open(self.name)
        except:
            raise ExamException("Can't open this File")
        
        return self.analize_data

    def analize_data(self, data_file):
        try:
            str_data = data_file.read()
        except:
            raise ExamException("File read this File")
        
        rows_data = str_data.split("\n")

        result = []

        for item in rows_data:    
            
            row_data = item.split(",")
            
            if(len(row_data) >= 2):
                valid_row = True
                
                if not ("-" in row_data[0]):
                    valid_row = False
                else:
                    row_date = row_data[0].split("-")
                    try:
                        row_year = int(row_date[0])
                        
                        #Aerei inesistenti prima del 1900
                        if(row_year < 1900):
                            valid_row = False

                    except:
                        valid_row = False

                    try:
                        row_month = int(row_date[1])
                        
                        #Aerei inesistenti prima del 1900
                        if(row_month < 1 or row_month > 12):
                            valid_row = False

                    except:
                        valid_row = False


                try:
                    n_passeggeri = int(row_data[1])

                    if(n_passeggeri < 0):
                        valid_row = False
                except:
                    valid_row = False

                #I dati esistono perchè valid_row è True
                if(valid_row == True):
                    row = [row_data[0], n_passeggeri]
                    result.append(row)

        return self.check_order_duplicates(result)

    def check_order_duplicates(self, data_list):
        if not (len(data_list) == 0):
            date = data_list[0][0]
            
            for item in data_list[1:]:
                if item[0] < date:
                    raise ExamException("Dates are not ordered")
                elif item[0] == date:
                    raise ExamException("There are duplicates in Dates")
                date = item[0]

        return data_list


def detect_similar_monthly_variations(time_series, years):
    for item in years:
        if not isinstance(item, int):
            raise ExamException("Years List is not correct")
        presente = False
        for item2 in time_series:
           if int(item2[0].split("-")) == item:
               presente = True
               break

        if not presente:
            raise ExamException("Selected Date is not found in the File")

        if not years[0] + 1 == years[1]:
            raise ExamException("Years List is not correct")

    anno1 = [None for i in range(12)]
    anno2 = [None for i in range(12)]
    
    year1 = years[0]
    year2 = years[1]

    for item in time_series:
        if(year1 == int(item[0].split("-")[0])):
            anno1[int(item[0].split("-")[1]) - 1] = item[1]
        elif(year2 == int(item[0].split("-")[0])):
            anno2[int(item[0].split("-")[1]) - 1] = item[1]

    result = []
    for index in range(1,12):
        is_in_range = False

        if anno1[index] != None and anno2[index] != None and anno1[index - 1] != None and anno2[index - 1] != None:
            if abs(anno1[index] - anno1[index - 1] - anno2[index] + anno2[index - 1]) <= 2:
                is_in_range = True

        result.append(is_in_range)

    return result

