# 숫자 시퀀스의 평균 계산하기
def getMean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues) > 0 \
        else float('nan')

my_list = [2, 2, 4, 4, 6, 6, 8, 8]
print("Output #135 (mean): {!s}".format(getMean(my_list)))
