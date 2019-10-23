#-*- coding: utf-8 -*-
import os
import time
import textManager
import rule
#import main  #import main이라고 써놔서 main.py에서 여기로 넘어올떄 충돌생기는것 같아서 주석처리했습니다. ( by 계)

def printStudentinfo(code):
    #학생정보출력
    os.system('cls')
    print("=" * 18, end='')
    print("[마이페이지]", end='')
    print("=" * 21)
    myInfo=textManager.readText_Student_c(code) #code학번학생의 정보 배열 받아옴
    print(myInfo[1] + " ( " + myInfo[0] + " ) ")
    print("hp : " + myInfo[2])
    print("수강내역")
    classArr=textManager.Re_UserInfo(code)
    for i in range(len(classArr)):
        print('  -  '+classArr[i][1]) # @를 띄어쓰기로 치환후 출력 #강의 정보들 출력!
    print("="*50)
    return myInfo
def printTeacherinfo(code):
    #선생님정보출력
    os.system('cls')
    print("=" * 18, end='')
    print("[마이페이지]", end='')
    print("=" * 21)
    myInfo=textManager.readText_Teacher_c(code) #code학번학생의 정보 배열 받아옴
    print(myInfo[1]+" ( "+myInfo[0]+" ) ")
    print("hp : "+myInfo[2])
    print("개설강의")
    classArr=textManager.Re_UserInfo(code)
    for i in range(len(classArr)):
        print('  -  '+classArr[i][1]) # @를 띄어쓰기로 치환후 출력 #강의 정보들 출력!
    print("="*50)
    return myInfo
def modifyInfo(code,myInfo):
    #정보수정화면
    while True:
        printModifyinfo(code)
        print("1. 이름수정\n2. 전화번호수정\n3. 뒤로가기")
        choice = input("원하시는 항목을 선택해 주세요 : ")

        if rule.numberRule(choice)==0: #숫자입력규칙 적용, import main 주석처리해서 __import__로 즉석해서 import함
            time.sleep(2)
            os.system('cls')
            return 0
        if choice == '1':
            if modifyName(code,myInfo)==1:
                print("정보가 성공적으로 수정되었습니다.")
                time.sleep(2)
                os.system('cls')
                #마이페이지 화면으로 돌아갑니다.
                return 0
        elif choice == '2':
            if modifyPhone(code,myInfo)==1:
                print("정보가 성공적으로 수정되었습니다.")
                time.sleep(2)
                os.system('cls')
                 # 마이페이지 화면으로 돌아갑니다.
                return 0
        elif choice == '3':
            return 0
        else:
            print("선택지 내의 숫자를 입력하여주세요")
            time.sleep(2)
            os.system('cls')
            #printModifyinfo(code) 기획서에 맞게 수정(by최)
            return 0
def printModifyinfo(code):
    #정보수정화면 정보 출력화면
    os.system('cls')
    print("=" * 18, end='')
    print("[정보 수정]", end='')
    print("=" * 21)
    if code[0] == 'S':
        myInfo = textManager.readText_Student_c(code)
    else:
        myInfo = textManager.readText_Teacher_c(code)
    print(myInfo[1] + " ( " + myInfo[0] + " ) ")
    print("hp : " + myInfo[2])
    print("=" * 50)
def modifyName(code,myInfo):
    #이름수정
    print(myInfo[1], end="")
    newName = input(">>>")
    if len(newName) > 10:
        print("형식에 어긋납니다.다시 입력하십시오")
        time.sleep(2)
        os.system('cls')
        return 0
    else:
        textManager.RenewalName(code, myInfo[1], newName) #수정!
        return 1
def modifyPhone(code,myInfo):
    #전화번호수정
    print(myInfo[2], end="")
    newPhone = input(">>>")
    if len(newPhone) == 11 and newPhone.isdecimal():  # type(newPhone)=='int' int로 하면 len이 안되는거 같아오
        # 전화번호수정하고
        textManager.RenewalName(code, myInfo[2], newPhone) #수정!
        return 1
    else:
        print("형식에 맞게 다시 입력하십시오.")
        time.sleep(2)
        os.system('cls')
        return 0
def screen(code):
    while True:
        # 메인화면 출력
        if code[0]=='S':
            myInfo=printStudentinfo(code)
        else:
            myInfo =printTeacherinfo(code)
        print("1. 정보수정\n2. 뒤로가기")
        choice = input("원하시는 항목을 선택해 주세요 : ")

        #숫자입력규칙
        if rule.numberRule(choice)==0: #숫자입력규칙 적용, import main 주석처리해서 __import__로 즉석해서 import함
            time.sleep(2)
            os.system('cls')
            continue
        #메뉴 분기
        if choice == '1':
            #"1. 정보수정" 이동
            os.system('cls')
            modifyInfo(code, myInfo)
        elif choice == '2':
            #"2. 뒤로가기" 이동
            return 0
        else:
            print("선택지 내의 숫자를 입력하여주세요")  # 숫자입력규칙 적용필요
            time.sleep(2)
            os.system('cls')
            continue