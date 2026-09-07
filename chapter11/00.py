# 리스트

scores = [86, 92, 78, 66, 77, 100, 55, 25]

total = 0

for score in scores :
    total += score
print(total) 


avg = total / len(scores)



print(f"총 합계 점수는 {total}이고 인원은 {len(scores)}명입니다. 이때 평균은 {avg}입니다.")





# 그룹이 2그룹 상위(51~100) 하위(1~50) 그룹의 합계, 인원수 평균을 각각 출력하시오. 
scores = [86, 92, 78, 66, 77, 100, 55, 25, 10, 43, 50]

total_high = 0
total_low = 0

count_high = 0
count_low = 0

for score in scores :
    if score >= 51:
        total_high += score
        count_high += 1
    else:
        total_low += score
        count_low += 1

avg_high = total_high / count_high
avg_low = total_low / count_low

print(f"상위 그룹 총 합계 점수는 {total_high}이고 인원은 {count_high}입니다. 이때 평균은 {avg_high}입니다.")
print(f"하위 그룹 총 합계 점수는 {total_low}이고 인원은 {count_low}입니다. 이때 평균은 {avg_low}입니다.")
