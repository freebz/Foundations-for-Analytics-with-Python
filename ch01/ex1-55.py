# try-except-else-finally

# 긴 버전
try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("Output #138 (Error): {}".format(float('nan')))
    print("Output #138 (Error): {}".format(detail))
else:
    print("Output #138 (The mean is): {}".format(result))
finally:
    print("Output #138 (Finally): The finally block is excuted every time")
