# 100,000원 이상 → 10% 할인 안내
# 50,000원 이상  → 5% 할인 안내
# 그 외           → 할인 없음

total_price = int(input("상품 금액을 입력하세요 : "))
if total_price >= 100000 :
    print(f"10% 할인이 적용되어 최종 금액은 {int(total_price*0.9)}입니다.")
elif total_price >= 50000 :
    print(f"5% 할인이 적용되어 최종 금액은 {int(total_price*0.95)}입니다.")
else:
    print("할인 없음")