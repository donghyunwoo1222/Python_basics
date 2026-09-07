score = 60
if score >= 60:
    print("통과입니다.")
print("프로그램을 종료합니다.")



score = int(input("점수를 입력하세요 : "))
if score >= 90:
    print("A등급")
elif score >= 80:
    print("B등급")
elif score >= 70:
    print("C등급")
else:
    print("재시험 대상입니다.")



age = int(input("나이를 입력하세요 : "))
if age >= 20 and age < 65:
    print("일반 요금은 20,000원입니다.")
else:
    print("할인/무료 대상입니다.")



age = int(input("나이를 입력하세요 : "))
if age < 18 or age >= 65:
    print("할인 대상입니다.")
else:
    print("일반 요금입니다.")



day = "토요일"
if day == "토요일" or day =="일요일":
    print("주말입니다.")



order_amount = 40000
is_member = False
if order_amount >= 50000 or is_member:
    print("무료배송입니다.")
else:
    print("배송비는 3000원입니다.")

