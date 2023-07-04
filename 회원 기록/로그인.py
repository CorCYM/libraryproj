import cx_Oracle

def login(id,pw):
    try:
        conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
        cursor = conn.cursor()
        sql = "SELECT * FROM LIBUSER WHERE userid = :id and password = :pw"

        cursor.execute(sql,[str(id),str(pw)])
        result = cursor.fetchall()
        cursor.close()
        conn.close()

    except :
        print('로그인 실패')
        return False
    print(f'{result}계정 로그인')
    return True

def membership(id,pw):
    try:
        conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
        cursor = conn.cursor()
        sql = "insert into LIBUSER (userid,password) values (:1,:2)"

        cursor.execute(sql, (str(id), str(pw)))
        conn.commit()
        cursor.close()
        conn.close()
        print('회원가입 성공')
    except :
        print('회원가입 실패')
