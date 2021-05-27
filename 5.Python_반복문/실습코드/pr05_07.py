x=int(input("높이를 입력하시오:"))

for i in range(1,x+1):
    for j in range(x+1-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()