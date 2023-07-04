conn = cx_Oracle.connect('libraryDB/1234@10.10.21.33:1521/xe')

cursor = conn.cursor()

var1 = 'LEND_SEQ.NEXTVAL'
var2 = '1'
var3 = 'book2id'
var4 = date

sql = f"insert into LENDBOOK (LENDNUM, USERID, BOOKID, LENDDATE) values (LEND_SEQ.NEXTVAL, '{var2}', '{var3}', '{var4}')"

cursor.execute(sql)
conn.commit()

cursor.close()
conn.close()