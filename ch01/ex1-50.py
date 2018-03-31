# 딕셔너리 축약을 이용하여 특정 키-값 쌍들을 고르기
my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
my_results = {key : value for key, value in my_dictionary.items() if value > 10}
print("Output #133 (dictionary comprehension): {}".format(my_results))
