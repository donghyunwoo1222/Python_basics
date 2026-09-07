#temperature = 30

temperature = int(input("오늘의 기온을 입력하세요 : "))
if temperature > 30:
    print("오늘은 덥습니다.")
else:
    print("오늘은 날씨가 좋습니다.")
print("날씨 확인을 마쳤습니다.")



#score = 59
score = int(input("숫자를 입력하세요 : "))

print(f"{score}는 60보다 크거나 같은가? : {score >= 60}")
