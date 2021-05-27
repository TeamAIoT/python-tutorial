num=int(input("숫자:"))
result=True

for i in range(2,num):
    if num%i==0:
        result=False
        break

if result==False:
    print("소수가 아닙니다.")
else:
    print("소수입니다")
