from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/members/ 접속 시 views.py의 member_list 함수 실행
    path("", views.member_list, name="member_list"),
]