class Diff():
    def __init__(self, ratio=1):

        if not isinstance(ratio, (int,float)):
            raise ExamException('Ratio non è intero')
        
        if ratio <= 0:
            raise ExamException('Impossibile dividere per 0')
        
        self.ratio = ratio

    def compute(self, value_list):

        if not isinstance(value_list, list):
            raise ExamException('Non è una lista')
        
        if len(value_list) <= 1:
            raise ExamException('La lista valori non è                 valida')

        for values in value_list:
            if not isinstance(values, (int, float)):
                raise ExamException('No differenza con                     stringa')
            
        diff_list = []
        i = 0
        j = i + 1

        while j < len(value_list):
            
            diff = (value_list[j] - value_list[i])/self.ratio

            diff_list.append(diff)
            
            i = i + 1
            j = j + 1

        #if self.ratio != 1:
            #for idx, diff in enumerate(diff_list):
                #diff_list[idx] = diff_list[idx] /                          self.ratio
                
        return diff_list

class ExamException(Exception):
    pass


#diff = Diff(2.5) 
#result = diff.compute([2,4,8,16])
#print(result)