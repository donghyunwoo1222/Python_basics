# 과제 A 카페 주문 금액

coffee_price = 4500
cake_price = 6500
total_price = coffee_price*3 + cake_price*2
print(total_price)

# 작성한 코드 : 위와 같다
# 실행 전 예상 결과 : 커피 가격과 케익 가격을 명시하고 곱한 값을 총가격으로 하여 print 했기 때문에 26500원이 나올 것으로 예상
# 실제 실행 결과 : 26500원이 출력됨
# 사용한 연산자와 그 역할 : *(곱하기)
# AI에게 질문했다면 질문 내용과 내가 직접 검증한 결과 : X

# 과제 B 학습 시간 변환

total_minutes = 385
hours = total_minutes // 60
minutes = total_minutes % 60
print(hours,"시간",minutes,"분")

# 작성한 코드 : 위와 같다.
# 실행 전 예상 결과 : 6 시간 25 분 
# 실제 실행 결과 : 6 시간 25 분
# 사용한 연산자와 그 역할 : //(나누고 버림), %(나머지를 나타냄)
# AI에게 질문했다면 질문 내용과 내가 직접 검증한 결과 : X 

# 과제 C 직사각형 계산

width = 12
height = 8
rectangle_area = width * height
print(rectangle_area)

print(rectangle_area > 100)

width += 3
rectangle_area = width * height

print(rectangle_area)

# 작성한 코드 : 
width = 12
height = 8
rectangle_area = width * height
print(rectangle_area)

print(rectangle_area > 100)

width += 3

print(rectangle_area)
# 실행 전 예상 결과 : 96, false, 120
# 실제 실행 결과 : 96, false, 96
# 사용한 연산자와 그 역할 : *, >, +=
# AI에게 질문했다면 질문 내용과 내가 직접 검증한 결과 : 코드를 올리고 정답이 아니라 힌트를 달라고 함. 
# AI가 파이썬은 알아서 바뀐 내용을 갱신해주지 않으니 너비를 바꿨다면 다시 곱셈공식을 실행해서 담아주는 코드가 들어가야 한다고 알려줌.
#실제 검증 결과
width = 12
height = 8
rectangle_area = width * height
print(rectangle_area)

print(rectangle_area > 100)

width += 3
rectangle_area = width * height

print(rectangle_area)