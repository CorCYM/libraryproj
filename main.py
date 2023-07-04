import login
import search
import lendsystem



loginmenu = '''
===============
1. 로그인
2. 회원가입
===============
'''


main_menu = '''
============
1. 조회
2. 대여
3. 반납
============
'''


search_menu ='''
===============================
1. 도서 검색
2. 저자 검색
3. 총합 도서관 검색
4. 선택한 도서 장바구니에 추가
5. 돌아가기
===============================
'''
lend_book = '''
=================
1.대출
2.돌아가기
=================
'''

return_book = '''
================
1.반납
2.돌아가기
================
'''

def log_menu():
    global id
    print(loginmenu)
    user_input = int(input())
    if user_input==1:
        id = input('로그인 아이디 입력')
        pw = input('로그인 비밀번호 입력')
        log_in = login.login(id,pw)
        if log_in==True:
            Mainmenu()
        else:
            log_menu()

    elif user_input==2:
        id = input('회원가입 아이디 입력')
        pw = input('회원가입 비밀번호 입력')
        membership = login.membership(id,pw)
        membership
        log_menu()



def Mainmenu():
    print(main_menu)
    user_input = int(input("번호를 입력하세요:"))
    lend = lendsystem.lendLib(id)
    if user_input == 1:
        print('조회로 이동합니다.')
        Searching()
    elif user_input == 2:
        print("대여로 이동합니다.")
        lend_book = lend.lendtry()
        lend_book
    elif user_input == 3:
        print("반납으로 이동합니다.")
        Return_lib = lend.returnlib()
        Return_lib        
    else:
        print("잘못입력하셨습니다")
        Mainmenu()



def Searching():
    print(search_menu)
    lend = lendsystem.lendLib(id)
    user_input = int(input("번호를 입력하세요:"))
    if user_input == 1:
        bookname = search.search_bookname()
        bookname
        Searching()
    elif user_input ==2:
        writer = search.search_writer()
        writer
        Searching()
    elif user_input ==3:
        libname = search.search_library()
        libname
        Searching()
    elif user_input ==4:
        print('선택 도서 장바구니 추가')
        lend_book = lend.lendtry()
        lend_book
    elif user_input ==5:
        print("뒤로가기")
        Mainmenu()
    else:
        print('잘못입력하셨습니다')
        print(f'다시 입력해주세요:{search_menu}')
        Searching()



# def lend_book():
#     user_input = int(input("번호를 입력하세요:"))
#     if user_input == 1:
#         print("대출")
#     elif user_input==2:
#         print("뒤로가기")
#         Mainmenu()
#     else:
#         print('잘못입력하셨습니다')
#         lend_book()

# def Return_book():
#     user_input = int(input("번호를 입력하세요:"))
#     if user_input ==1:
#         print("반납")
#     elif user_input ==2:
#         print("뒤로가기")
#         Mainmenu()
#     else:
#         print('잘못입력하셨습니다')
#         Return_book()



log_menu()


