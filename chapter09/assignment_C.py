saved_id = "python"
saved_password = "1234"

id = input("아이디를 입력하세요 : ")
password = input("비밀번호를 입력하세요 :")

if id==saved_id and password == saved_password:
    print("로그인 성공")
else:
    print("아이디 또는 비밀번호를 확인하세요")