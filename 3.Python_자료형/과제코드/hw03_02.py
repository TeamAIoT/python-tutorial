scores = [[75, 83, 90], [86, 86, 73], [76, 95, 83], [89, 96, 69], [89, 76, 93]]
student6 = [10, 100, 23]
scores.append(student6)
print(scores)
sum =(scores[0][1]+scores[1][1]+scores[2][1]+scores[3][1]+scores[4][1]+scores[5][1])
avg = sum/6
print("합계 : {0}  평균 : {1:.2f}".format(sum,avg))