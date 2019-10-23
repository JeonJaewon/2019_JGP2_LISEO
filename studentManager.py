#-*- coding: utf-8 -*-
import time
import os
import textManager
import rule
#import main    #여기도 충돌나는거같은거 수정

#함수 정의
def checkIfTeacher(code): # 고유번호가 학생인지 선생인지 검사
    if code[0] == 'S':
        return False
    elif code[1] == 'T':
        return True

def printStudentList(): # 모든 학생 리스트 출력
    studentInfo=textManager.readText_Student()
    os.system('cls')
    print("=" * 18, end='')
    print("[학생 관리]", end='')
    print("=" * 21)
    print('학생 리스트')
    for studentData in studentInfo:
        # 수강중인 강의 목록 가져오기
        if len(studentData)<=1:
            break
        classListString=''
        classList=textManager.studentID_to_classList(studentData[0])
        for classCode in classList:
            classListString+=classCode+', '
        classListString=classListString[:-2]

        #출력
        print(studentData[0] + ' '+studentData[1] + ' ('+studentData[2]+') '+ '-'+' '+classListString)
    print('==================================')

def addStudentInfo(): # 학생 정보 추가
    print("새로 추가할 학생의 이름을 입력하세요 '('10자 이내 문자')'")
    studentName = input() or '입력 실패'
    if len(studentName) > 10:
        print("입력 형식에 맞게 다시 입력하십시오.")
        return

    print("새로 추가할 학생의 전화번호를 입력하세요 '('11자리 숫자')'")
    studentTel = input()
    if len(studentTel) != 11:
        print("입력 형식에 맞게 다시 입력하십시오.")
        return

    print("학생이 성공적으로 추가되었습니다.")
    # -정보 추가-
    textManager.Re_Student(studentName,studentTel)

def deleteStudentInfo(): # 학생 정보 삭제
    deleteCode=input("삭제하려는 학생의 고유번호를 입력하세요. : ") or '입력 실패'
    # 존재하는 학생인지 확인
    if(textManager.Re_Student('1', deleteCode) == -1):
        print("입력한 학생의 정보를 찾을 수 없습니다.")
        return
    else:
        print("해당 학생의 정보가 성공적으로 삭제되었습니다.")
    # -정보 제거-

def studentManagerScreen(code):
    while True:
        if checkIfTeacher(code) == False: #선생이 아니면 종료
            print("사용자는 해당 기능에 접근할 수 없습니다.")
            time.sleep(2)
            break

        printStudentList()
        print(" " * 5, '1. 학생 정보 추가')
        print(" " * 5, '2. 학생 정보 삭제')
        print(" " * 5, '3. 뒤로가기')
        menu = input('원하시는 항목을 선택해 주세요 : ') or '입력 실패'
        if rule.numberRule(menu)==0:
            time.sleep(2)
            os.system('cls')
            continue
        menu = int(menu)

        if menu == 1:
            addStudentInfo()
        elif menu == 2:
            deleteStudentInfo()
        elif menu == 3:
            break
        else:
            print("메뉴에 없는 번호입니다")
            #기획서에 메인메뉴가 아닌 학생 관리 재출력이라고 되어있어서 수정
            #time.sleep(2)
            #os.system('cls')
            #break
        time.sleep(2)
        os.system('cls')
