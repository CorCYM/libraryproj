# import 로그인v2
import 조회기능.search_v as search_v


pront = '''
==========================================

광산구 도서 관리 시스템에 오신걸 환영합니다.

==========================================
'''

print(pront)

main = '''
============
1. 조회
2. 대여
3. 반납
============
'''
print(main)

serch ='''
===============================
1. 도서 검색
2. 저자 검색
3. 총합 도서관 검색
4. 선택한 도서 장바구니에 추가
5. 돌아가기
===============================
'''
lendering = '''
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

def Mainmenu():
    user_input = int(input("번호를 입력하세요:"))
    if user_input == 1:
        print('조회로 이동합니다.')
        print(serch)
        Serch()
    elif user_input == 2:
        print("대여로 이동합니다.")
        print(lendering)
        Lendering()
    elif user_input == 3:
        print("반납으로 이동합니다.")
        print(return_book)
        Rbook()
    else:
        print("잘못입력하셨습니다")
        print(f"다시입력해주세요:{main}")
        return Mainmenu()

# def Serch():
#     user_input = int(input("번호를 입력하세요:"))
#     if user_input == 1:
#         print('도서 검색:')
#         Serchi
#     elif user_input ==2:
#         print('저자 검색:')
#     elif user_input ==3:
#         print('총합 도서관 검색')
#     elif user_input ==4:
#         print('선택 도서 장바구니 추가')
#     elif user_input ==5:
#         print("뒤로가기")
#         print(main)
#         Mainmenu()
#     else:
#         print('잘못입력하셨습니다')
#         print(f'다시 입력해주세요:{serch}')
#         return Serch()

def Lendering():
    user_input = int(input("번호를 입력하세요:"))
    if user_input == 1:
        print("대출")
    elif user_input==2:
        print("뒤로가기")
        print(main)
        Mainmenu()
    else:
        print('잘못입력하셨습니다')
        print(f'다시 입력해주세요:{lendering}')
        return Lendering()

def Rbook():
    user_input = int(input("번호를 입력하세요:"))
    if user_input ==1:
        print("반납")
    elif user_input ==2:
        print("뒤로가기")
        print(main)
        Mainmenu()
    else:
        print('잘못입력하셨습니다')
        print(f'다시 입력해주세요:{return_book}')
        return Rbook()


Mainmenu()


