from numpy import savetxt
savetxt('output_file.txt', data)


savetxt('output_file.txt', data, fmt='%d')
savetxt('output_file.csv', data, fmt='%.2f', delimiter',')


column_headings_list = ['var1', 'var2', 'var3']
header_string ','.join(column_headings_list)
savetxt('output_file.csv', data, fmt='%.2f', delimiter=',', \
        comments='', header=header_string)
