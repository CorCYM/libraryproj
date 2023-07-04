import cx_Oracle

bookname = [0]
conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
cursor = conn.cursor()
sql = "SELECT * FROM libbook WHERE bookname = %s"
value = ([str(bookname)])
cursor.execute(sql,[str(bookname)])
result = cursor.fetchall()
cursor.close()
conn.close()


def serching():
    user_input = str(input("도서 이름을 입력하세요:"))
    if bookname == user_input:
        print(result)
    else:
        print('없는 항목입니다.')
   
