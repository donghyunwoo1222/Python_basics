
total =0

for number in range(1, 6):
    if number % 2 == 0:
        
        print(f"{number}는 짝수입니다.")
        total += number
        print(f"모두 더한 값은{total}입니다.")