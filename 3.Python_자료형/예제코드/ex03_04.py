a = ['e','a','c','b','d']
b = [3,1,2,5,4,6]
index = a.index('c') #위치 반환
b.insert(1,8) #요소 삽입
print(a)
print(b)
print("제거 후")
a.remove('a') # a 리스트의 'a'제거
popB = b.pop(5) # b 리스트의 5번째 값 반환 후 제거
print(popB)
print(a)
print(b)