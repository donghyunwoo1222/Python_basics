
#append -> 맨 마지막에 붙인다. (인덱스 넣지 않아도 됨)

fruits = ["사과","바나나"]
fruits.append("포도")
print(fruits)


todo = []
todo.append("책 읽기")
todo.append("운동하기")
todo.append("복습하기")
print(todo)


#insert -> 인덱스를 정해서 그 자리에 넣는다.

fruits = ["사과", "포도"]
fruits.insert(1, "바나나")
print(fruits)


#extend -> 여러 리스트를 이어붙인다. 

fruits = ["사과", "바나나"]
more_fruits = ["포도", "딸기","키위"]

print("원래 fruits의 과일 갯수 :", len(fruits))

fruits.extend(more_fruits)
print(fruits)

print("extend 후 fruits의 과일 갯수 :", len(fruits))


