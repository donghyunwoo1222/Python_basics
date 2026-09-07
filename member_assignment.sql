# Part  1. PostgreSQL Schema와 Table 만들기

create schema practice;

CREATE TABLE practice.members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER,
    joined_at DATE
);

# Part 2. INSERT와 SELECT로 회원 데이터 관리하기

insert into practice.members 
(name, email, age, joined_at)values
('김민준', 'minjun.kim@example.com', 24, '2023-03-14'),
('이서연', 'seoyeon.lee@example.com', 29, '2022-11-02'),
('박지훈', 'jihoon.park@example.com', 31, '2021-07-20'),
('최유나', 'yuna.choi@example.com', 22, '2024-01-08'),
('정도윤', 'doyoon.jung@example.com', 27, '2023-09-30');

#전체조회

select*from practice.members;

#이름과 이메일만 조회

select name, email from practice.members;

#25세 이상 회원 조회

select * from practice.members
where age >= 25;

#특정 이름의 회원 조회 (김민준)

select * from practice.members
where name = '김민준';
# SQL에서 같다는 등호 하나, ""는 문자열이 아니라 테이블명이나 칼럼명 같은 식별자를 감쌀때 쓰는 표기

#나이가 많은 순서로 조회

select * from practice.members
order by age desc;

#가입일 순서로 조회

select * from practice.members
order by joined_at asc;

# Part 3. UPDATE와 DELETE로 데이터 변경하기

# 특정 회원의 정보 수정

update practice.members
set age=30
where member_id = 1;

select * from practice.members;
# member_id가 1인 데이터의 age를 30으로 수정 

# 특정 회원 삭제

delete from practice.members 
where member_id = 5;
# member_id가 5인 데이터 삭제

# Part 4. 집계 함수를 이용한 회원 데이터 분석

select count(*) from practice.members;

select avg(age) from practice.members;

select max(age) from practice.members;

select min(age) from practice.members;

select count(*) from practice.members
where age >= 25;

 # 도전 문제
 # 가장 최근에 가입한 회원 조회하기
 
select * from practice.members
order by joined_at desc
limit 1;
# pandas의 head()처럼 상위 몇개만 보여주는 기능은 limit이 한다.

# 평균 나이보다 나이가 많은 회원 조회하기

select * from practice.members
where age >= (select avg(age) from practice.members);
# where 조건 안에는 avg같은 집계함수를 바로 사용이 불가능하다.
# 평균니이를 따로 구하고, 그 값을 where 값에 넣는 방법을 사용해야함
# 이럴때 서브쿼리를 사용함. ()안에 또 다른 select 구문을 넣어서 그 결과값 하나를 숫자처럼 쓰는 방식

# 이메일 주소를 기준을 특정 회원 검색하기

select * from practice.members
where email = 'seoyeon.lee@example.com';

# 원하는 조건 2개 이상을 함께 사용하여 회원 조회하기

select * from practice.members
where age >= 30 or name = '이서연';

## 확인 질문

다음 질문에 본인의 말로 짧게 답변해주세요.

1. `PRIMARY KEY`는 왜 필요한가요?
- PK는 테이블 안에서 데이터를 식별하기 위해 사용한다. 중복이 안되고, not null이라는 특징이 있다. 
2. `WHERE` 없이 `UPDATE` 또는 `DELETE`를 실행하면 어떤 문제가 발생할 수 있나요?
- where 없이 사용하면 특정 데이터를 지정하는게 아니라 전체가 다 지워지거나 수정될 수 있다. 
3. `SELECT *`와 필요한 컬럼만 선택하는 SQL의 차이는 무엇인가요?
- *은 전체를 다 선택하는 것이고, 필요한 컬럼만 넣어서 선택할 수도 있다. 
4. `COUNT()`와 `AVG()`는 각각 어떤 값을 계산하나요?
- count()는 괄호 안의 데이터 수를 세고, avg()는 괄호 안의 값들의 평균을 계산한다. 
5. Python에서 데이터를 처리하는 것과 DB에서 SQL로 데이터를 조회하는 것의 차이를 어떻게 이해했나요?
- python에서는 pandas로 데이터르 처리하고, DB에서는 PostgreSQL로 데이터를 처리했는데, python에서는 print로 값을 출력하고, sql에서는 select로 출력하는데 차이가 있다.
- 또한 python은 데이터를 활용해서 직접 코드를 짜고 계산하지만, sql은 DBMS를 활용해서 계산과 필터링이 이루어져서 대용량 데이터를 다룰때 부담이 적다는 차이가 있다. 