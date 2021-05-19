n1=int(input())
n2=int(input())
n3=int(input())

if n1<n2:
    if n1<n3:
        print("Min =",n1)
    else:
        print("Min =",n3)
else:
    if n2<n3:
        print("Min =",n2)
    else:
        print("Min =",n3)