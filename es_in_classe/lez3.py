def sum_csv(file_name):
      
    values = []
    my_file = open(file_name, 'r')
    vuoto = True
    
    for line in my_file:
        elements = line.split(',')
    
        if elements[0] != 'Date':
            value = elements[1]
            values.append(float(value))
            vuoto = False
        
    if vuoto == False:
        return sum(values)
    else:
        return None
    
    file.close()

#print(sum_csv('shampoo_sales.csv')) 
#print(sum_csv('empty_file.csv'))
#(sum_csv('shampoo_sales.csv'))
#print(sum_csv('sum_vuoto.csv'))
