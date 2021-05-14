s1 = set([1,2,3,4,5])
l1 = [4,5,6,8]
l2 = [10,23,54]
s2 = set(l1)
print(s2)
s2.add(2)
print(s2)
print(s1)
s1.update(l2)
print(s1)
s1.remove(1)
print(s1)