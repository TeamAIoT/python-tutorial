f=open("C:/Users/owner/Desktop/7.Python_파일입출력/실습파일/실습.txt",'w')
while True:
    data=input("파일에 입력할 문구를 작성하시오:")
    if data=="stop":
        break
    f.write(data+"\n")
f.close()
