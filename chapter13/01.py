#sentence = "나는 대한민국 서울 구로에서 파이썬 공부를 하고 있습니다." #단어 100개 이상 
#words = sentence.split()

#print(type(words))
#print(words)

# sentence에서 3회 이상 등장하는 단어는 무엇일까요? 각 단어와 빈도수를 출력하시오. 
# 단, 오늘 배운 딕셔너리를 활용해주세요. 지금까지 배우지 않은 기능 사용하지 말 것. 

sentence = "나는 대한민국 서울 구로에서 파이썬 공부를 열심히 하고 있습니다. 파이썬은 정말 재미있고 유용한 프로그래밍 언어입니다. 파이썬을 이용하면 다양한 인공지능과 데이터 분석 작업을 쉽게 할 수 있습니다. 대한민국 IT 산업의 중심지 서울에서 파이썬을 배우는 것은 정말 멋진 일입니다. 구로 디지털단지 근처에서 파이썬 스터디 모임을 하며 파이썬 실력을 키워나가고 있습니다. 매일 파이썬 코드를 작성하고 파이썬 문법을 익히며 파이썬 프로젝트를 진행합니다. 파이썬 기초부터 파이썬 심화 과정까지 차근차근 공부하면서 파이썬의 매력에 푹 빠져 있습니다. 주변 친구들도 파이썬을 많이 공부하고 있어서 함께 파이썬 문제를 풀며 파이썬 실력을 높이고 있습니다. 앞으로도 계속 파이썬을 활용하여 멋진 프로그램을 만들고 파이썬 전문가가 되기 위해 최선을 다할 것입니다. 파이썬 화이팅!"

words = sentence.split()
over_three = {}
for word in words:
    if word not in over_three:
        over_three[word] = 1
    else:
        over_three[word] = over_three[word]+1
for word, count in over_three.items():
    if count >= 3:
        print(f"{word}: {count}회")

        