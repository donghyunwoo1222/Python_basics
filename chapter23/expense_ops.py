import psycopg2

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "your_password",  # 환경에 맞게 수정
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            date VARCHAR(10) NOT NULL,
            category VARCHAR(50) NOT NULL,
            description VARCHAR(100) NOT NULL,
            amount INTEGER NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_expense_db(date, category, description, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (date, category, description, amount) VALUES (%s, %s, %s, %s)",
        (date, category, description, amount)
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_expenses_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, category, description, amount FROM expenses ORDER BY date DESC, id DESC;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return [
        {"id": r[0], "date": r[1], "category": r[2], "description": r[3], "amount": r[4]}
        for r in rows
    ]

def delete_expenses_batch(id_list):
    """선택된 여러 항목을 일괄 삭제"""
    if not id_list:
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ANY(%s)", (id_list,))
    conn.commit()
    cursor.close()
    conn.close()