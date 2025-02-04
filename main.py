﻿#-*- coding: utf-8 -*-
import os
import time
import login
import mypage
import ClassView
import myClass
import studentManager
import rule

def screen(code):
    while True:
        os.system('cls')
        print("="*18, end='')
        print("[메인 화면]", end='')
        print("=" * 21)
        print(" "*18,'1. 마이페이지')
        print(" "*18,'2. 강의 정보 열람')
        print(" "*18,'3. 내 강의')
        print(" "*18,'4. 학생 관리')
        print(" "*18,'5. 종료')
        print("="*50)
        select= input("원하시는 항목을 선택해 주세요 : ") or '입력실패'
        if select=='입력실패' :
            print("접근 할 선택지 번호를 입력해 주세요.")
            time.sleep(2)
            os.system('cls')
            continue
        elif rule.numberRule(select)==0:
            time.sleep(2)
            os.system('cls')
            continue
        if select=='1': #마이페이지->MyPage
            mypage.screen(code)
        elif select=='2': #강의 정보 열람->ClassView
            ClassView.start(code)
        elif select=='3': #내 강의->MyClass
            myClass.myClass(code)
        elif select=='4': #학생 관리->StudentCare
            studentManager.studentManagerScreen(code)
        elif select=='5': #종료
            exit(0) # return 으로 해도 무방
        else:
            print("1-5사이의 항목을 선택해 주세요.")    # 숫자입력규칙 적용필요
            time.sleep(2)
            os.system('cls')
code = login.start() # code 어떤 학생 어떤 선생인지 체크하는 변수
screen(code)