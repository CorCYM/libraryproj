import cx_Oracle

def search_bookname():
    bookname = input("도서를 검색합니다: ")
    conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
    cursor = conn.cursor()
    sql_bookname = "SELECT BOOKNAME,BOOKID FROM LIBBOOK WHERE BOOKNAME LIKE '%' || :1 || '%'"
    cursor.execute(sql_bookname, (bookname,))
    result_bookname = cursor.fetchall()
    cursor.close()
    conn.close()
    if result_bookname:
        print("검색 결과:",result_bookname)
    else:
        print('해당 도서를 찾을 수 없습니다.')
        return search_bookname
    


def search_writer():
    writer = input("저자를 검색합니다: ")   
    conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
    cursor = conn.cursor()  
    sql_writer = "SELECT WRITER,BOOKNAME FROM LIBBOOK WHERE WRITER LIKE '%' || :1 || '%'"
    cursor.execute(sql_writer, (writer,))
    result_wirter = cursor.fetchall()
    cursor.close()
    conn.close()
    if result_wirter:
        print("검색 결과:",result_wirter,end='')
    else:
        print('해당 저자를 찾을 수 없습니다.')
        return search_writer


def search_library():
    libname = input("도서를 검색합니다: ")
    conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
    cursor = conn.cursor()
    sql_libname = "SELECT BOOKNAME,LIBNAME FROM LIBBOOK WHERE BOOKNAME LIKE '%' || :1 || '%'"
    cursor.execute(sql_libname, (libname,))
    result_libname = cursor.fetchall()
    cursor.close()
    conn.close()
    if result_libname:
        print("검색 결과:", result_libname,end='')
    else:
        print('해당 도서를 찾을 수 없습니다.')
        return search_library





