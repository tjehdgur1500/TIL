import sqlite3

conn = sqlite3.connect("filePath", isolation_level=None)

c = conn.cursor()

# 전체 데이터 조회
c.execute('SELECT * FROM dbinfo')
print(c.fetchall())

# 원하는 컬럼만 조회
numbers = (1,)
c.execute('SELECT * FROM dbinfo WHERE num=?', numbers)

# 컬러 다중 조회
numbers = (2, 3, 4)
c.execute('SELECT * FROM dbinfo WHERE num IN (?,?,?)', numbers)

# dump 파일 쓰기
with conn:
    with open('filePath', 'w') as f:
        for sql in conn.iterdump():
            print(f.write("%s\n" % sql))


# 데이터 수정
c.execute('UPDATE dbinfo SET price=? WHERE num=?', ('3000', 1))

# 데이터 삭제

# 전체 삭제
c.execute('DELETE FROM dbinfo')

# 원하는 데이터 row 삭제
c.execute('DELETE FROM dbinfo WHERE num IN (?,?)', (1, 2))

# 이외에도 다양하게 mix 해서 사용가능
