# sort() 함수를 이용하여 리스트를 인프레이스로 정렬하기
# 이는 리스트가 변경된다는 것을 의미한다.
# 기존 리스트의 변경 없이 리스트를 정렬하려면, 우선 사본을 만든다.
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
print("Output #88: {}".format(unordered_list))
list_copy = unordered_list[:].sort()
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))
