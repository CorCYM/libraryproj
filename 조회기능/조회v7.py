import cx_Oracle


bookname = input("입력하세요: ")
# bookid = input("입력하세요: ")   
# writer = input("입력하세요: ")


class Serch:
    def __init__(self,bookname,bookid,writer):
        self.bookname = bookname
        self.bookid = bookid
        self.writer = writer

    def searching(bookname):
        conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
        cursor = conn.cursor()
        sql_bookname = "SELECT BOOKNAME FROM LIBBOOK WHERE BOOKNAME LIKE '%' || :1 || '%'"
        cursor.execute(sql_bookname, (bookname,))
        result_bookname = cursor.fetchall()
        cursor.close()
        conn.close()
        if result_bookname:
            print("검색 결과:",result_bookname)
        else:
            print('해당 도서를 찾을 수 없습니다.')
            return False

    def searching(bookid):
        conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
        cursor = conn.cursor()  
        sql_bookid = "SELECT BOOKID FROM LIBBOOK WHERE BOOKID LIKE '%' || :1 || '%'"
        cursor.execute(sql_bookid, (bookid,))
        result_bookid = cursor.fetchall()
        cursor.close()
        conn.close()
        if result_bookid :
            print("검색 결과:",result_bookid)
        else:
            print('해당 도서를 찾을 수 없습니다.')
            return False

    def searching(writer):
        conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
        cursor = conn.cursor()
        sql_writer = "SELECT WRITER FROM LIBBOOK WHERE WRITER LIKE '%' || :1 || '%'"
        cursor.execute(sql_writer, (writer,))
        result_writer = cursor.fetchall()
        cursor.close()
        conn.close()
        if result_writer:
            print("검색 결과:", result_writer)
        else:
            print('해당 도서를 찾을 수 없습니다.')
            return False

# 하나의 검색 값으로 3가지 조건 중 하나만 만족해도 검색이 가능하게.

Serch