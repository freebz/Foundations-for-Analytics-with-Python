# 파일 읽기
# 하나의 텍스트 파일 읽기
print("Output #139: ")
input_file = sys.argv[1]
filereader = open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()
