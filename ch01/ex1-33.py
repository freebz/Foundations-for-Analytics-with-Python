# sorted() 함수를 이용하여 리스트들의 특정 위치에 따라 리스트 정렬하기
my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))
