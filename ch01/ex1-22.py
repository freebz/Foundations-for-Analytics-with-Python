# date 객체를 특정 형식의 문자열으로 만들기
print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))

# Output #50: 03/25/2018
# Output #51: Mar 25, 2018
# Output #52: 2018-03-25
# Output #53: March 25, 2018
