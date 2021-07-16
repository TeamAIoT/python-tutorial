def add_many(*args):
    result=0
    for i in args:
        result = result+i
    return result

result=add_many(4,5,6,7)
print(result)