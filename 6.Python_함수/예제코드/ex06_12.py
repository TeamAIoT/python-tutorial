def countdown(n):
    if n==0:
        print("finish!")
    else:
        print(n)
        countdown(n-1)

countdown(3)