f=open("새파일.txt",'a')
for i in range(11,21):
    data = "%d 번째 줄입니다.\n"%i
    f.write(data)
f.close()