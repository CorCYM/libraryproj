## 도서관 대여기능


import cx_Oracle

conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')

cursor = conn.cursor()

sql = '''
select * from libbook
'''

cursor.execute(sql)
result = cursor.fetchall()

cursor.close()
conn.close()

from datetime import *
now = datetime.now()
date = now.date()
# print(date)

booknum = []
for i in result:
    num = i[3]
    booknum.append(num)

# print(booknum)

# bookname = []
# for i in result:
#     bkname = i[4]
#     bookname.append(bkname)
# print(bookname)



#db와 연동 lendbook에서 기존 대여 목록 가져오기
conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')

cursor = conn.cursor()

sql = '''
select * from lendbook
'''

cursor.execute(sql)
result2 = cursor.fetchall()

cursor.close()
conn.close()

persons_lendlist = result2

## print(persons_lendlist)

def lend():
    while True:
        user_input = input("대출 할 서적의 등록번호를 입력하세요.\n종료를 원하시면 z을 누르세요 :\n")
        if ('z' in user_input) or ('ㅋ' in user_input):
            if len(lendlist) == 0:
                print("등록번호를 잘못 입력하셨습니다.")
                continue
            else:
                break
        if user_input not in booknum:
            print("도서 목록에 없습니다.")
        elif user_input in persons_lendlist:
            print("이미 대여 중인 도서입니다.")
        else:
            lendlist.append(user_input)
    return lendlist
    print("대출 희망 도서 목록 번호는 {0}입니다".format(",".join(lendlist)))

lendlist = [] #장바구니

lend()

while True:
    user_input2 = input("대출 희망 목록 중 추가를 원하신다면 1을 눌러주세요 \n목록 중 삭제를 원하신다면 2를 눌러주세요 \n대출을 확정하시겠다면 0을 눌러주세요 :\n")
    if user_input2 == '0':
        break
    if user_input2 == '1':
        lend()
    if user_input2 == '2':
        while True:
            user_input3 = input("삭제할 도서 등록번호를 입력해주세요. \n대출화면으로 돌아가고 싶으시다면 z를 눌러주세요 : \n" )
            if ('z' in user_input3) or ('ㅋ' in user_input3):
                break
            else:
                lendlist.remove(user_input3)
            print(f"현재 대출희망 도서목록은 {lendlist}입니다")



print("---"*3 + "대출 진행 중입니다." + "---"*3)


person_lendlist = [] #개인 대출 목록
person_lendlist.append(lendlist)
#
if len(lendlist) > 6:
    print("추가 대출이 불가능합니다. 기존 대출 도서를 반납해주세요")
else:
    print("대출 완료. 대출 날짜 {0}, 대출 기한은 {1}까지 입니다".format(date, date + timedelta(days=5)))
    print(f"님의 대출 목록은 : {person_lendlist} 입니다.")

##person_lendlist를 db의 lendbook에 업데이트
# conn = cx_Oracle.connect('libadmin/1234@10.10.21.33:1521/xe')
#
# cursor = conn.cursor()
#
# var1 = num
# var2 = id
# var3 = person_lendlist
# var4 = date
#
# sql = f"insert into LENDBOOK (LENDNUM, USERID, BOOKID, LENDDATE) values ('{var1}', '{var2}', '{var3}', '{var4}')"
#
# cursor.execute(sql)
# cursor.commit
# cursor.close()
# conn.close()

lendlist = [] #대출 과정 종료 이후 장바구니 비우기

# print(person_lendlist)


## 도서관 반납기능

def returnlib():
    while True:
        user_input4 = input("반납하실 도서번호를 입력하십시오 :\n 반납 프로그램 종료는 0를 입력하십시오")
        if user_input4 == '0':
            break
        elif user_input4 in person_lendlist:
            user_input5 = input("반납하시겠습니까? 반납은 1번 취소는 2번을 입력해주세요.")
            if user_input5 == 2:
                break
            else:
                person_lendlist.remove(user_input4)
                print(f"님의 대출 목록은 : {person_lendlist} 입니다.")
        else:
            print("반납 목록에 해당 도서가 존재하지 않습니다.")

