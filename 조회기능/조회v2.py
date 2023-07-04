import cx_Oracle
cursor.execute(sql)
result = cursor.fetchall()

cursor.close()
conn.close()


def Serching(self,vo):
    self.conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
    cur = self.conn.cursor()
    sql = "select bookname from libbook"
    vals = (vo.id, vo.pw, vo.name,