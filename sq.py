##삭제 쿼리

conn = cx_Oracle.connect('test1/1234@localhost:1521/xe')
cursor = conn.cursor()
#
# var1 = 'LEND_SEQ.NEXTVAL'
# var2 = 'userid'
# var3 = 'book2d'
# var4 = date
sql = "delete from LENDBOOK where BOOKID = 'bookid'"

cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()