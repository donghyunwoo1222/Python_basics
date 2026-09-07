#주문 금액 계산 프로그램

customer = input("고객 이름: ").strip()

product = input("상품명: ").strip()

price = int(input("상품 가격: "))

quantity = int(input("수량: "))

total = price * quantity

print(f"고객: "{customer}\n)

print(f"문길동님이 파이썬 입문서 2개를 주문했습니다. 총 36000원입니다."