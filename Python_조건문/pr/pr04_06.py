n1=int(input())
n2=int(input())
sum=n1+n2
if sum%3==0 and sum%6==0:
    print("%d is multiple of 3 and 6"%sum)
elif sum%3==0:
    print("%d is multiple of 3"%sum)
elif sum%6==0:
    print("%d is multiple of 6"%sum)
else :
    print("%d is not multiple of 3 or 6"%sum)