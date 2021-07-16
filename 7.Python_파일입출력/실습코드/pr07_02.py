f=open("C:/Users/owner/Desktop/7.Python_파일입출력/실습파일/실습.txt",'r')

line=len(f.readlines())
f.close()

f=open("C:/Users/owner/Desktop/7.Python_파일입출력/실습파일/실습.txt",'r')

while True:
    num=int(input("줄 수를 입력하시오:"))
    if num>line:
        continue

    for i in range(0,num):
        data=f.readline()
        print(data,end="")
    break
f.close()
