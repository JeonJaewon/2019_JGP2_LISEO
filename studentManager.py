import time
import os
import textManager

#함수 정의
def checkIfTeacher(code): # 고유번호가 학생인지 선생인지 검사
    if code[0] == 'S':
        return False
    elif code[1] == 'T':
        return True

def printStudentList(): # 모든 학생 리스트 출력
    print()

def addStudentInfo(): # 학생 정보 추가
    print("새로 추가할 학생의 이름을 입력하세요 '('10자 이내 문자')'")
    studentName = input()
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
    print("삭제하려는 학생의 고유번호를 입력하세요. : ")
    deleteCode = input()
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
            break

        printStudentList()
        print("=" * 50)
        print(" " * 18, '1. 학생 정보 추가')
        print(" " * 18, '2. 학생 정보 삭제')
        print(" " * 18, '3. 뒤로가기')
        print("=" * 50)
        print("원하시는 항목을 선택해 주세요 : ")
        menu = int(input())

        if menu == 1:
            addStudentInfo()
        elif menu == 2:
            deleteStudentInfo()
        elif menu == 3:
            break
        else:
            print("메뉴에 없는 번호입니다")
            time.sleep(2)
            os.system('cls')
            break
        time.sleep(2)
        os.system('cls')