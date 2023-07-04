import cx_Oracle

class Search:
    def searching(self, search_term, search_type="bookname"):
        conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
        cursor = conn.cursor()
        if search_type == "bookname":
            sql = "SELECT BOOKNAME FROM JANGDEOK WHERE BOOKNAME LIKE '%' || :1 || '%'"
        elif search_type == "bookid":
            sql = "SELECT BOOKID FROM JANGDEOK WHERE BOOKID LIKE '%' || :1 || '%'"
        elif search_type == "writer":
            sql = "SELECT WRITER FROM JANGDEOK WHERE WRITER LIKE '%' || :1 || '%'"
        else:
            print("잘못된 검색 유형입니다.")
            return False
        
        cursor.execute(sql, (search_term,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        
        if results:
            print(f"검색 결과 ({search_type}): {results}")
        else:
            print("해당 도서를 찾을 수 없습니다.")
            return False



search = Search()
search_term = input("검색어를 입력하세요: ")
search.searching(search_term)

Search.searching()