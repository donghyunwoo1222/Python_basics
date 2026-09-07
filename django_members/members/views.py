from django.shortcuts import render
from .models import Member


def member_list(request):
    # 1. member_id 기준 오름차순으로 모든 회원 데이터 조회
    # (SQL: SELECT * FROM members ORDER BY member_id ASC;)
    members = Member.objects.all().order_by("member_id")

    # 2. HTML 템플릿에 전달할 데이터를 dictionary 형태로 포장
    context = {
        "members": members,
    }

    # 3. 'members/member_list.html' 템플릿을 데이터와 함께 렌더링
    return render(request, "members/member_list.html", context)