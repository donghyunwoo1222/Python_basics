from expense_ops import init_db, add_expense_db, get_expenses_db

def add_expense():
    date = input("날짜(YYYY-MM-DD): ").strip()
    category = input("카테고리: ").strip()
    description = input("내용: ").strip()
    
    if not date or not category or not description:
        print("날짜, 카테고리, 내용은 비워 둘 수 없습니다.")
        return
        
    try:
        amount = int(input("금액: "))
    except ValueError:
        print("금액은 정수로 입력해 주세요.")
        return
        
    if amount <= 0:
        print("금액은 0보다 큰 값으로 입력해 주세요.")
        return

    # CSV에 저장하는 대신 DB 함수 호출
    add_expense_db(date, category, description, amount)
    print("지출 내역이 데이터베이스에 추가되었습니다.")

def show_expenses():
    expenses = get_expenses_db()
    if not expenses:
        print("등록된 지출이 없습니다.")
        return
        
    print("\n=== 지출 내역 (DB 연동) ===")
    number = 1
    for expense in expenses:
        print(
            f"{number}. {expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"{expense['amount']:,}원"
        )
        number += 1

def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)

def calculate_by_category(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount
    return category_totals

if __name__ == "__main__":
    # 프로그램 시작 시 DB 및 테이블 초기화
    init_db()
    
    while True:
        print("\n=== 개인 지출 관리 (콘솔 + DB) ===")
        print("1. 지출 추가")
        print("2. 지출 목록")
        print("3. 지출 요약(합계)")
        print("0. 종료")
        
        choice = input("메뉴 선택: ").strip()
        
        # 최신 데이터 항상 DB에서 불러오기
        current_expenses = get_expenses_db()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            print("\n--- 지출 요약 ---")
            print(f"전체 지출 합계: {calculate_total(current_expenses):,}원")
            print("카테고리별 합계:", calculate_by_category(current_expenses))
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("메뉴 번호를 다시 선택해 주세요.")