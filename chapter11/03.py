#remove -> 값을 찾아 삭제
#pop -> 값을 출력하고 삭제
#del -> 인덱스 값을 찾아 삭제 (내장함수)

fruits = ["사과", "바나나", "포도", "딸기"]

fruits.remove("바나나")
print(fruits)

removed = fruits.pop(1)
print(removed)
print(fruits)

del fruits[0]
print(fruits)