tags = ["Python", "AI", "Python", "Data", "AI"]

# set을 쓰지 말고 list 기능만 써서 unique_tags를 구현하시오.
# 수도코드(의사코드)로 작성해줘.

#일단 for로 돌려.  이걸 반복하다가 그담에 if로 이미 있으면? 지운다? 반복. 출력.

unique_tags = []

for i in tags:
    if i not in unique_tags:
        unique_tags.append(i)
    
print(unique_tags)

## AI에게 받은 힌트. 값을 집어넣기(append) 전에, "이 값이 unique_tags 안에 없는지(not in)" 먼저 확인하고 나서 넣어야 하지 않을까요? 순서를 살짝 바꿔보세요!
# not in이 안에 없는지 확인하는 메소드라는 것을 알지 못해 어려움이 있었다. 

#처음 세운 코드
# unique_tags = []
#for i in tags:

#    unique_tags.append(i)

#    if i in unique_tags:

#        unique_tags.remove(i)    <- 이 부분에서 아예 remove를 해버리니 두 값이 모두 사라져버려 문제가 있었던 것 같다. 

#print(unique_tags)