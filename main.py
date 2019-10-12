import os
import time
import login
import ClassView
import studentManager
import mypage
#import ClassView
import myClass
#import StudentCare

def screen(code, classCode, roomCode, schedule):
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
            mypage.mypagePrint(code)
        elif select==2: #강의 정보 열람->ClassView
            print('you select : ', select)
            ClassView.start(code)
        elif select==3: #내 강의->MyClass
            # print('you select : ', select)
            myClass.myClass(code)
        elif select==4: #학생 관리->StudentCare
            print('you select : ', select)
            studentManager.studentManagerScreen(code)
        elif select==5: #종료
            exit(0) # return 으로 해도 무방
        else:
            print("1-5사이의 항목을 선택해 주세요.")    # 숫자입력규칙 적용필요
            time.sleep(2)
            os.system('cls')

code = login.start() # code 어떤 학생 어떤 선생인지 체크하는 변수

# test용
screen(code)
    #메인화면 출력