
fruits = ["사과", "바나나", "사과", "포도", "사과"]

print(len(fruits))

print("바나나" in fruits)

print(fruits.count("사과"))

print(fruits.index("포도"))

taget = "딸기"

if taget in fruits:
    fruits.remove(taget)
print(fruits)