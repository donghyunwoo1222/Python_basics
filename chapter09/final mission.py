#FINAL MISSION — 간단한 주문 배송 안내 프로그램

# 주문 금액이 50,000원 이상이면 무료배송
# 회원이면서 주문 금액이 30,000원 이상이어도 무료배송

customer_name = input("이름을 입력하세요 : ")
total_price = int(input("주문 금액을 입력하세요 : "))
member_answer = input("회원인가요? (y/n) :").strip().lower()

if total_price >= 50000:
    print(f"{customer_name}님은 무료배송 대상자입니다.")
elif member_answer == "y" and total_price >= 30000:
    print(f"{customer_name}님은 무료배송 대상자입니다.")
else:
    print("배송비는 3000원입니다.")