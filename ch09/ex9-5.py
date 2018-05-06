from pandas import read_excel
from numpy import array
myDataFrame = read_excel('myExcelInputFile.xlsx')
data = array(myDataFrame)
print(data)
