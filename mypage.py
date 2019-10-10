import os
import time
import textManager

def mypagePrint(code):
    #권한에 따라 마이페이지 정보 출력
    if code[0]=='S':
        printStudentinfo(code)
    else:
        printTeacherinfo(code)



def printStudentinfo(code):
    #학생정보출력
    print("="*50)
    #myInfo=textManager.readStudentText(code) code학번학생의 정보 배열 받아옴
    #print(myInfo[1}" ( "myInfo[0]" ) ")
    #print("hp : "myInfo[2])
    #print("수강내역")
    #for i in myInfo-3
    #   print(myInfo[i+3])
    print("="*50)


def printTeacherinfo(code):
    #선생님정보출력
    print("="*50)
    #myInfo=textManager.readTeacherText(code) code학번학생의 정보 배열 받아옴
    #print(myInfo[1}" ( "myInfo[0]" ) ")
    #print("hp : "myInfo[2])
    #print("개설강의")
    #for i in myInfo-3
    #   print(myInfo[i+3])
    print("="*50)

def modifyInfo(code):
    #정보수정화면
    printModifyinfo(code)
    choice=input("1. 이름수정\n2. 전화번호수정\n3. 뒤로가기")
    if choice==1:
        if modifyName(code) :
            print("정보가 성공적으로 수정되었습니다.")
            time.sleep(2)
            os.system('cls')
            screen(code)#마이페이지 화면으로 돌아갑니다.
    elif choice==2:
        if modifyPhone(code) :
            print("정보가 성공적으로 수정되었습니다.")
            time.sleep(2)
            os.system('cls')
            screen(code)  # 마이페이지 화면으로 돌아갑니다.
    elif choice==3:
        return 0
    else:
        print("선택지 내의 숫자를 입력하여주세요")  # 숫자입력규칙 적용필요
        time.sleep(2)
        os.system('cls')
        printModifyinfo(code)


def printModifyinfo(code):
    #정보수정화면 정보 출력화면
    print("="*50)
    if code[0]=='S':
        # myInfo=textManager.readStudentText(code)
    else:
        # myInfo=textManager.readTeacherText(code)
    # print(myInfo[1}" ( "myInfo[0]" ) ")
    # print("hp : "myInfo[2])

def modifyName(code):
    #이름수정
    if code[0]=='S':
        # myInfo=textManager.readStudentText(code)
    else:
        # myInfo=textManager.readTeacherText(code)
    #print(myInfo[1],end='')
    newName=input(">>>")
    if len(newName)>10 :
        print("형식에 어긋납니다.다시 입력하십시오")
        time.sleep(2)
        os.system('cls')
        modifyInfo(code)
    else:
        #정보수정하고
        return 1

def modifyPhone(code):
    #전화번호수정
    if code[0]=='S':
        # myInfo=textManager.readStudentText(code)
    else:
        # myInfo=textManager.readTeacherText(code)
    #print(myInfo[2],end='')
    newPhone=input(">>>")
    if type(newPhone)=='int' and len(newPhone)==11 :
        #전화번호수정하고
        return 1
    else:
        print("형식에 어긋납니다.다시 입력하십시오")
        time.sleep(2)
        os.system('cls')
        modifyInfo(code)


def screen(code):
    mypagePrint(code)
    choice=input("1. 정보수정\n2. 뒤로가기")
    if choice==1:
        os.system('cls')
        if(not modifyInfo(code)):
            os.system('cls')
            screen(code)
    elif choice==2:
        return 0
    else:
        print("선택지 내의 숫자를 입력하여주세요")  # 숫자입력규칙 적용필요
        time.sleep(2)
        os.system('cls')
        screen(code)

