import csv
from numpy import array
file = open('myCSVInputFile.csv', 'r')
file_reader = csv.reader(file)
data = []
for row_list in file_reader:
    row_list_floats = [float(value) for value in row_list]
    data.append(row_list_floats)
file.close()
data = array(data)
print(data)
