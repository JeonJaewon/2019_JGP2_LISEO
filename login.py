#-*- coding: utf-8 -*-
import time
import os

def start():
    teacher = open("teacher.txt", 'r', encoding='UTF-8-SIG')
    student = open("student.txt", 'r', encoding='UTF-8-SIG')

    LoginInfo = []
    while True:
        TeacherData = teacher.readline()
        if not TeacherData:
            break
        TeacherLogin = TeacherData.split('@', maxsplit=3)
        LoginInfo.append(TeacherLogin[0])

    while True:
        StudentData = student.readline()
        if not StudentData:
            break
        StudentLogin = StudentData.split('@', maxsplit=3)
        LoginInfo.append(StudentLogin[0])

    while True:
        os.system('cls')
        print("="*50)
        print(" "*22, "LISEO")
        print("="*50)  # 로그인 화면의 화면 제목

        name = input("사용자의 고유번호를 입력해주세요 (단, 종료를 원하시면 q를 입력해주세요.) :")  or '입력 실패'
        if name == 'q':
            exit(0)
        elif name in LoginInfo:
            os.system('cls')
            return name
            #break
        elif name == '입력 실패':
            print("값을 입력해 주세요.")
            time.sleep(2)
            os.system('cls')
        else:
            print("해당하는 고유번호가 없습니다. 다시 입력해 주세요.")
            time.sleep(2)
            # 화면 지우기 추가할 것=>파이참에는 없는 기능?
            os.system('cls')
            #검거 print(start())  # 2번 반복하여 불러올 시 에러 생김


    teacher.close()
    student.close()
# name과 불러온 정보 일치시 화면 지운 후 메인 화면 출력 if name == rnumber.
# 고유번호 존재하지 않을 시 오류메시지 출력 후 2초 뒤 모든 화면 삭제 및 로그인 화면 출력

