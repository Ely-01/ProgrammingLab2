#da controllare
class CSVFile():
  def __init__(self, name):
    self.name=name

  def get_data(self):
    try:
      file= open(self.name, 'r')
      values=[]
      for line in file:
        elements=line.strip('\n').split(',')
        if elements[0]!='Date':
          values.append(elements)
      file.close()
    except Exception as e:
      print('Errore {}'.format(e))

    return values
