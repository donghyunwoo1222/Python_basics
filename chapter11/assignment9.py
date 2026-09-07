#점수 5개를 리스트에 저장한다.
#학생 수를 출력한다.
#총점, 최저점, 최고점, 평균을 출력한다.
#80점 이상 점수만 출력한다.
#마지막에 오름차순으로 정렬한다.

test1 = [80, 80, 80, 80, 80]
test2 = [0, 25, 50, 75, 100]
test3 = [100, 90, 80, 70, 60]
test4 = [25, 60, 75, 50, 90]

total_test = test1 + test2 + test3 + test4
avg = sum(total_test) / len(total_test)
print(len(total_test))
print(sum(total_test))
print(min(total_test))
print(max(total_test))
print(avg)

high_scores = []
for test in total_test:
    if test >= 80:
        high_scores.append(test)
high_scores.sort()
print(high_scores)