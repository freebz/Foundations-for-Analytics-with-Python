# 파일 작성하기
# 하나의 텍스트 파일 작성하기
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' 'j']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("Output #142: Output written to file")
