pin = "881120-1068234"
s1 = "19"+pin[:2]+"년 "+pin[2:4]+"월 "+pin[4:6]+"일" # +사용
print(s1)
s2 = "19%s년 %s월 %s일"%(pin[:2],pin[2:4],pin[4:6]) #직접 format
print(s2)
s3 = "19{0}년 {1}월 {2}일".format(pin[:2],pin[2:4],pin[4:6])
print(s3)