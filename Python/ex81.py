# 파이썬 데이터베이스 (sqllite, MariaDB, MySQLDB, MongoDB)
import sqlite3
print('버전 출력 : ', sqlite3.sqlite_version)
try :
    conn = sqlite3.connect("sqlite_db")    # DB 연결자 생성
    cursor = conn.cursor()      # sql 실행 객체 생성

    sql = 'create table if not exists mem(name text(10), tel text(15), addr text(50))'
    cursor.execute(sql)

    cursor.execute("insert into mem values('김성민', '010-5136-3155', '롯데타워72층')")
    cursor.execute("insert into mem values('양지은', '010-4275-2345', '양양')")

    cursor.execute("select * from mem")
    rows = cursor.fetchall()

    print("회원 테이블 정보")
    for row in rows :
        print(row)

except Exception as e :
    print("DB 오류 : ", e)
    conn.rollback()
finally :
    cursor.close()
    conn.close()