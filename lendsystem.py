import cx_Oracle
from datetime import *
# conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
#
# cursor = conn.cursor()
#
# sql = '''
# select * from libbook
# '''
#
# cursor.execute(sql)
# result = cursor.fetchall()
#
# cursor.close()
# conn.close()
#
# from datetime import *
# now = datetime.now()
# date = now.date()
# # print(date)



# lendlist = []  # 장바구니
# person_lendlist = [] #개인 대출 목록
# persons_lendlist = [] # DB 내의 전체 대출 목록

class lendLib(object):
    def __init__(self,object):
        self.lendlist = []
        self.person_lendlist = []
        self.persons_lendlist = []
        self.id = object

        conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
        cursor = conn.cursor()
        sql = '''
        select * from libbook
        '''
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()


        self.now = datetime.now()
        self.date = self.now.date()

        self.booknum = []
        for i in result:
            num = i[3]
            self.booknum.append(num)

        conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
        cursor = conn.cursor()

        sql = '''
        select * from lendbook
        '''

        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        self.lentnum = []
        for i in result:
            num1 = i[2]
            self.lentnum.append(num1)

        # self.lentid = []
        # for i in result:
        #     num2 = i[1]
        #     self.lentid.append(num2)


    def lendtry(self):
        while True:
            user_input1 = input("대출 할 서적의 등록번호를 입력하세요.\n대출도서 결정 또는 프로그램종료를 원하시면 z을 누르세요 :\n")
            if ('z' in user_input1) or ('ㅋ' in user_input1):
                if len(self.lendlist) == 0:
                    print("프로그램을 종료합니다.")
                    break
                else:
                    break
            if user_input1 not in self.booknum:
                print("도서 목록에 없습니다.")
            if user_input1 in self.lentnum:
                print("이미 대여 중인 도서입니다.")
            else:
                self.lendlist.append(user_input1)
                print("대출 희망 도서 목록 번호는 {0}입니다".format(",".join(self.lendlist)))
        if len(self.lendlist) != 0:
            self.lendmodify()
        return self.lendlist

    def lendmodify(self):
        while True:
            user_input2 = input("대출 희망 목록 중 추가를 원하신다면 1을 눌러주세요 \n목록 중 삭제를 원하신다면 2를 눌러주세요 \n대출을 확정하시겠다면 0을 눌러주세요 :\n")
            if user_input2 == '0':
                break
            if user_input2 == '1':
                self.lendtry()
            if user_input2 == '2':
                while True:
                    user_input3 = input("삭제할 도서 등록번호를 입력해주세요. \n대출화면으로 돌아가고 싶으시다면 z를 눌러주세요 : \n")
                    if ('z' in user_input3) or ('ㅋ' in user_input3):
                        break
                    else:
                        self.lendlist.remove(user_input3)
            else:
                print("잘못 누르셨습니다.")
        print(f"현재 대출희망 도서목록은 {self.lendlist}입니다")
        print("---" * 3 + "대출 진행 중입니다." + "---" * 3)
        self.lendcomfirm()
        return self.lendlist

    def lendcomfirm(self):
        
        conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
        cursor = conn.cursor()
        sql = "select count(userid) from lendbook where userid = '{0}'".format(self.id)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        if result[0][0] + len(self.lendlist) >= 6:
            print("추가 대출이 불가능합니다. 기존 대출 도서를 반납해주세요")
            
        else:
            print("대출 날짜 {0}, 대출 기한은 {1}까지 입니다".format(self.date, self.date + timedelta(days=5)))
            self.person_lendlist.append(self.lendlist)  ## 대출 도서를 db의 대출 목록에 추가

            var2 = str(self.id)
            var4 = self.date
            for lends in self.person_lendlist:
                for lend_one in lends:
                    var3 = lend_one
                    conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
                    cursor = conn.cursor()
                    sql = f"insert into LENDBOOK values (LEND_SEQ.NEXTVAL, '{var2}', '{var3}', '{var4}')"
                    cursor.execute(sql)
                    conn.commit()
                    cursor.close()
                    conn.close()
           
                    
        print(f"  {self.id} 님의 대출 목록은 : {self.person_lendlist} 입니다.")  ##  DB의 내 전체 대출 목록을 보여줌


    def returnlib(self):
        while True:
            user_input4 = input("반납하실 도서번호를 입력하십시오 :\n반납 프로그램 종료는 0를 입력하십시오\n")
            if user_input4 == '0':
                print("종료되었습니다")
                break

            conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
            cursor = conn.cursor()
            sql = '''
            select * from lendbook
            '''
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            conn.close()

            self.persons_lendlist = [] ## DB내 전체 인원의 도서 대여 리스트
            for i in result:
                lendnum = i[2]
                self.persons_lendlist.append(lendnum)

            if user_input4 in self.persons_lendlist:
                user_input5 = input("반납하시겠습니까? 반납은 1번 취소는 0번을 입력해주세요.")
                if user_input5 == '0':
                    break
                if user_input5 == '1':
                    self.persons_lendlist.remove(user_input4)
                    # print(f"{self.id}님의 대출 목록은 : {self.persons_lendlist} 입니다.")
                    
                    conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
                    cursor = conn.cursor()

                    sql = "delete from LENDBOOK where BOOKID = '{0}'".format(user_input4)

                    cursor.execute(sql)
                    conn.commit()
                    cursor.close()
                    conn.close()

                    conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
                    cursor = conn.cursor()
                    sql = "select * from lendbook where userid = '{0}'".format(self.id)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    cursor.close()
                    conn.close()

                    self.person_lendlist = [] ## DB내 특정 ID의 대여 목록
                    for i in result:
                        yourlent = i[2]
                        self.person_lendlist.append(yourlent)
                        
                    print(f"{self.id}님의 대출 목록은 : {self.person_lendlist} 입니다.")

                else:
                    print("올바른 키를 입력해주세요.")
            else:
                print("반납 목록에 해당 도서가 존재하지 않습니다.")