# 날짜 문자열로부터 특정 형식의 datetime 객체를 생성하기
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')

# 다른 date 형식을 지닌 4가지 문자열에 기반한
# 각각 2종류의 datetime 객체들과 date 객체들
print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))

# 날짜 부분만 출력하기
print("Output #56: {!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime(date4, '%B %d, %Y'))))
