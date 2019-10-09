import os
import time
import login
import studentManager
#import MyPage
#import ClassView
#import MyClass

def screen():
    while True:
        print("="*50)
        print(" "*18,'1. 마이페이지')
        print(" "*18,'2. 강의 정보 열람')
        print(" "*18,'3. 내 강의')
        print(" "*18,'4. 학생 관리')
        print(" "*18,'5. 종료')
        print("="*50)

        select=int(input("원하시는 항목을 선택해 주세요 : "))
        if select==1: #마이페이지->MyPage
            print('you select : ', select)
            break
        elif select==2: #강의 정보 열람->ClassView
            print('you select : ', select)
            break
        elif select==3: #내 강의->MyClass
            print('you select : ', select)
            break
        elif select==4: #학생 관리->StudentCare
            print('you select : ', select)
            studentManager.studentManagerScreen(code)
        elif select==5: #종료
            exit()
        else:
            print("1-5사이의 항목을 선택해 주세요.")#숫자입력규칙 적용필요
            time.sleep(2)
            os.system('cls')

code = login.start() # code 어떤 학생 어떤 선생인지 체크하는 변수

screen()
    #메인화면 출력