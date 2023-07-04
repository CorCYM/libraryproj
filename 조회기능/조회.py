import cx_Oracle

conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')

cursor = conn.cursor()

sql = '''
select BOOKNAME from JANGDEOK
'''


cursor.execute(sql)
result = cursor.fetchall()

cursor.close()
conn.close()

print(result)