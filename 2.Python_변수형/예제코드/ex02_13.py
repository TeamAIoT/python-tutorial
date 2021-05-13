#정렬
s1 = "{0:<10}".format("hi")#왼쪽
s2 = "{0:^10}".format("hi")#가운데
s3 = "{0:>10}".format("hi")#오른쪽
print(s1+"|"+s2+"|"+s3)
#공백채우기
s4 = "{0:=^10}".format("hi")
print(s4)
