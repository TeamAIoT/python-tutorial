#2개 값 넣기
number = 10
day = "three"
s1 = "I ate {0} apples. {1} days.".format(number, day)
print(s1)
#이름으로 넣기
s2 = "I ate {number} apples. {day} days.".format(number=10, day=3)
print(s2)