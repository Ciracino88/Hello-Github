#! /usr/bin/env python3

import sqlite3 # sqlite3 모듈 임포트

# 접속 객체 생성 (이 객체를 통해 데이터와 관련된 명령들을 주고 받는다)
con = sqlite3.connect(':memory:')

# sales 테이블을 만들고 데이터를 집어넣는다
# VARCHAR, FLOAT, DATE는 각각 문자열, 실수, 날짜 필드를 뜻한다. (VARCHAR 내부의 숫자는 문자열의 최대 길이를 뜻함)
query = """CREATE TABLE sales
            (customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date DATE);"""

# query 안에 있는 SQL 명령어를 실행한다
con.execute(query)

# 데이터베이스의 변화를 저장한다
con.commit()

# 튜플 형식의 리스트 data를 만든다.
data = [('alice', 'notepad', 2.50, '2021-01-01'),
        ('anna', 'note', 4.15, '2021-01-02'),
        ('bow', 'pencil', 3.05, '2021-01-03'),
        ('leo', 'printer', 1.00, '2021-01-04')]

# data의 각 튜플을 대입하기 위한 변수 생성
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"

# statement의 ? 자리에 data 튜플을 삽입
con.executemany(statement, data)

# 데이터베이스 변화를 저장 (데이터베이스에 변경을 가했다면 반드시 이 작업을 해줘야한다)
con.commit()

# 데이터베이스로부터 데이터를 얻어오기 위한 변수
cursor = con.execute("SELECT * FROM sales")

# 데이터베이스에서 모든 결과물을 불러온다
rows = cursor.fetchall()

# 반복문으로 결과물을 하나씩 출력
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1

# 반복문이 끝나면 반복한 횟수를 출력하고 종료
print("row_counter: {}".format(row_counter))