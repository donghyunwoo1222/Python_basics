import random
from datetime import datetime, timedelta
from expense_ops import get_connection, init_db

# 카테고리별 현실적인 지출 항목 및 금액 범위 (가중치 반영)
SAMPLE_DATA = {
    "🍚 식비": {
        "items": ["구내식당 식권", "김치찌개 백반", "서브웨이 샌드위치", "버거킹 세트", "마라탕", "삼겹살 회식", "배달의민족 치킨", "초밥 정식", "칼국수와 만두", "돈까스"],
        "price_range": (8000, 35000),
        "step": 1000
    },
    "☕ 카페/간식": {
        "items": ["스타벅스 아메리카노", "메가커피 라떼", "투썸플레이스 케이크", "편의점 초콜릿/스낵", "공차 밀크티", "베이글 샌드위치", "에스프레소 바", "배스킨라빈스 파인트"],
        "price_range": (3000, 15000),
        "step": 500
    },
    "🚌 교통": {
        "items": ["지하철 정기권 충전", "카카오 T 택시", "광역버스 요금", "KTX 기차표", "공유 킥보드 이용", "주유비", "고속도로 톨게이트 비용"],
        "price_range": (1500, 60000),
        "step": 500
    },
    "🛍️ 쇼핑": {
        "items": ["유니클로 기본 티셔츠", "다이소 생활용품", "올리브영 스킨케어", "무신사 슬랙스", "쿠팡 생필품 주문", "나이키 양말 세트", "노트북 파우치"],
        "price_range": (5000, 95000),
        "step": 1000
    },
    "🏠 주거/통신": {
        "items": ["알뜰폰 통신비 요금", "전기/가스 관리비 분담", "원룸 인터넷 요금", "종량제 봉투 구매"],
        "price_range": (12000, 85000),
        "step": 1000
    },
    "🎉 문화/여가": {
        "items": ["CGV 영화 관람 및 팝콘", "넷플릭스 월간 구독료", "교보문고 IT 서적", "당구장 게임비", "스팀 인디게임 구매"],
        "price_range": (9900, 45000),
        "step": 1000
    },
    "💊 의료/건강": {
        "items": ["이비인후과 진료 및 처방약", "약국 종합감기약", "비타민 영양제", "치과 스케일링", "스포츠 헬스장 일일권"],
        "price_range": (4500, 50000),
        "step": 500
    },
    "기타": {
        "items": ["인생네컷 사진 촬영", "복권 구매", "증명사진 인화", "세탁소 드라이클리닝"],
        "price_range": (3000, 20000),
        "step": 1000
    }
}

def generate_dummy_records(count=100):
    records = []
    end_date = datetime.today()
    
    categories = list(SAMPLE_DATA.keys())
    # 일상에서 더 자주 발생하는 카테고리에 확률 가중치 부여 (식비/카페/교통 비중을 높임)
    weights = [0.35, 0.20, 0.15, 0.12, 0.05, 0.06, 0.04, 0.03]

    for _ in range(count):
        # 최근 45일 이내의 날짜 랜덤 분배
        random_days_ago = random.randint(0, 45)
        record_date = (end_date - timedelta(days=random_days_ago)).strftime("%Y-%m-%d")
        
        # 가중치 기반 카테고리 선정
        chosen_cat = random.choices(categories, weights=weights, k=1)[0]
        cat_info = SAMPLE_DATA[chosen_cat]
        
        # 상세 항목 랜덤 선택
        chosen_desc = random.choice(cat_info["items"])
        
        # 단위(step)에 맞춘 금액 생성
        min_p, max_p = cat_info["price_range"]
        step = cat_info["step"]
        amount = random.randrange(min_p, max_p + step, step)
        
        records.append((record_date, chosen_cat, chosen_desc, amount))
    
    # 일자 순 정렬
    records.sort(key=lambda x: x[0])
    return records

def insert_dummy_data():
    init_db()
    conn = get_connection()
    cursor = conn.cursor()
    
    dummy_data = generate_dummy_records(100)
    
    insert_query = """
        INSERT INTO expenses (date, category, description, amount)
        VALUES (%s, %s, %s, %s)
    """
    
    cursor.executemany(insert_query, dummy_data)
    conn.commit()
    cursor.close()
    conn.close()
    
    print(f"가짜 지출 데이터 {len(dummy_data)}건이 PostgreSQL에 성공적으로 삽입되었습니다!")

if __name__ == "__main__":
    insert_dummy_data()