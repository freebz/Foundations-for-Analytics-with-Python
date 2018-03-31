# 중괄호를 이용하여 딕셔너리 생성하기
# 각 쌍의 키와 값 사이에 콜론을 사용한다.
# len() 함수는 딕셔너리에 있는 키-값 쌍의 수를 센다.
empty_dict = { }
a_dict = {'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {!s} elements".format(len(a_dict)))
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict also has {!s} elements".format(len(another_dict)))
