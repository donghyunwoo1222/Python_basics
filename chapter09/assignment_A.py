age = int(input("나이를 입력하세요 : "))

if 0 <= age <= 7:
    print("미취학")
elif 8 <= age <= 13:
    print("초등학생 연령")
elif 14 <= age <= 16:
    print("중학생 연령")
elif 17 <= age <= 19:
    print("고등학생 연령")
else:
    print("성인")