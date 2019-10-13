#-*- coding: utf-8 -*-
import os
import time
import login
import mypage
import ClassView
import myClass
import studentManager

def screen(code):
    while True:
        print("="*50)
        print(" "*18,'1. 마이페이지')
        print(" "*18,'2. 강의 정보 열람')
        print(" "*18,'3. 내 강의')
        print(" "*18,'4. 학생 관리')
        print(" "*18,'5. 종료')
        print("="*50)

        select= input("원하시는 항목을 선택해 주세요 : ")
        rule(select)
        if select=='1': #마이페이지->MyPage
            print('you select : ', select)
            mypage.mypagePrint(code)
        elif select=='2': #강의 정보 열람->ClassView
            print('you select : ', select)
            ClassView.start(code)
        elif select=='3': #내 강의->MyClass
            # print('you select : ', select)
            myClass.myClass(code)
        elif select=='4': #학생 관리->StudentCare
            print('you select : ', select)
            studentManager.studentManagerScreen(code)
        elif select=='5': #종료
            exit(0) # return 으로 해도 무방
        else:
            print("1-5사이의 항목을 선택해 주세요.")    # 숫자입력규칙 적용필요
            time.sleep(2)
            os.system('cls')

def rule(number): #1.1에서 2^31-1의 정수 2.띄어쓰기 불가 3.최고 자릿수 0 불가 4.아스키코드 불가
    numMax="2147483647"
    for i in range(1,number.size()):
        if number[i]<'0' or number[i]>'9': #규칙2 띄어쓰기 와 규칙4 아스키코드
            print("숫자입력규칙에 어긋납니다.") #실험용
            return 0
    if number[0] == '0': #규칙 3 최고 자릿수 0
        print("숫자입력규칙에 어긋납니다.") #실험용
        return 0
    if number.length()>10:
        print("숫자입력규칙에 어긋납니다.") #실험용
        return 0
    if number.length()==10:
        for i in range(0,10):
            if number[i]>numMax[i]:
                print("숫자입력규칙에 어긋납니다.") #실험용
                return 0

code = login.start() # code 어떤 학생 어떤 선생인지 체크하는 변수
screen(code)
    #메인화면 출력