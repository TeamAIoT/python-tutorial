def my_max(*num):
    result=0
    for i in num:
        if result<=i:
            result=i
        else :
            pass
    return result

print(my_max(2,3,8,9,4,10,2,3,4))