# try-except

# 숫자 시퀀스의 평균 계산하기
def getMean(numericValues):
    return sum(numericValues)/len(numericValues)

my_list2 = []

# 잛은 버전
try:
    print("Output #137: {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("Output #137 (Error): {}".format(float('nan')))
    print("Output #137 (Error): {}".format(detail))
