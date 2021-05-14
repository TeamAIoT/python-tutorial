student = {'TH' : 99, 'JC': 17, 'SW': 18, 'JW':[1,2,3]}
print(list(student.keys()))
print(list(student.values()))
student['JW'] = 20
print(list(student.items()))
student.clear()
print(student)