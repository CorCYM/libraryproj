import cx_Oracle

def serching(bookname):
    conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
    cursor = conn.cursor()
    sql = "SELECT BOOKNAME FROM LIBBOOK =:5"
    cursor.execute(sql,bookname)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    print(result)
    # print('없는 항목입니다.')
    # return False

serching("BOOKNAME")

# def serching():
#     bookname = []
#     bookid = []
#     writer = []
    
#     if bookname 