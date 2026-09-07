# 과제 1. 상품 정보 저장

product = "파이썬 기초"
price = 28000
discount_rate = 0.15
on_sale = True
stock = 12

# 모범답안
#product_name
#price
#discount_rate
#is_on_sale
#stock

# 과제 2. 데이터 형 예상 
# product -> str
# price -> int
# discount_rate -> float
# on_sale -> bool
# stock -> int

# 과제 3. type()으로 검증
print(type(product))
print(type(price))
print(type(discount_rate))
print(type(on_sale))
print(type(stock))

# 과제 4. 형 변환
price_text = str(price)

print(type(price_text))
print(price_text)

# 과제 5. 오류 시험
int("파이썬")

ValueError: invalid literal for int() with base 10: '파이썬'
# 정수로 바꿀 수 없는 값을 정수로 바꾸려 한다는 오류메시지