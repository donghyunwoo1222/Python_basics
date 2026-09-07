#1번 문제

age = int(input("나이를 입력하세요 : "))
money = int(input("소지금액을 입력하세요 : "))
is_vip = input("vip 입니까(y/n) : ").strip().lower()

if (age >=20 and money >= 15000) or is_vip == "y":
    print("입장 가능합니다.")
else:
    print("입장 불가합니다.")


#2번 문제

user = ["김파이", 16, False ]
name = user[0]
age = user[1]
is_student = user[2]

if (age <18 and is_student == True) or age >= 65:
    print(f"{name}님은 할인 대상입니다.")
else:
    print(f"{name}님은 일반 요금 대상입니다.")


# 3번 문제

state = input("계정 잠금 상태를 입력하세요 (lock/unlock) : ").strip().lower()

if not state == "lock":
    print("로그인 성공")
else:
    print("계정이 잠겨 있어 로그인 할 수 없습니다.")


# 4번 문제

total_price = int(input("상품 구매 총액을 입력하세요 : "))
if total_price >= 200000:
    print(f"20% 할인이 적용되어 구매 총액은 {int(total_price*0.8)}입니다.")
elif 100000 <= total_price < 200000:
    print(f"10% 할인이 적용되어 구매 총액은 {int(total_price*0.9)}입니다.")
elif 50000 <= total_price < 100000:
    print(f"5% 할인이 적용되어 구매 총액은 {int(total_price*0.95)}입니다.")
else:
    print(f"할인 대상이 아닙니다. 결제 금액 : {total_price}원")


# 5번 문제

hours = int(input("주차한 시간을 입력하세요 : "))
is_light = input("경차 여부를 입력하세요(y/n) : ").strip().lower()
default_rates = hours * 2000

if is_light == "y" or hours >= 8:
    print(f"최종 주차요금은 {int(default_rates*0.5)}입니다.")
else:
    print(f"최종 주차요금은 {default_rates}입니다.")

 