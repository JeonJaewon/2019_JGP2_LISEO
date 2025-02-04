#-*- coding: utf-8 -*-
import os
import textManager
import time
import rule
#import main       #충돌나는거같아서 주석처리

def start(myID):
    myClassList=[]
    #사용자의 권한 확인
    if(myID[0] == 'S'):
        #학생입니다.
        isTeacher = False
        #자신의 수강강의 저장
        myClassList = textManager.readText_Class_stoc(myID)
    elif(myID[0] == 'T'):
        # 선생님입니다.
        isTeacher = True
        #자신의 개설강의 저장
        myClassList=textManager.readText_Class_ttoc(myID)
    else:
        print('error : 사용자의 ID 형식이 올바르지 않습니다.')
        time.sleep(2)
        return

    #메인메뉴
    while True:
        # 모든 강의정보 출력 ( 자신의 수강 or 개설강의 별표로 표시)
        os.system('cls')
        classInfo = textManager.readText_Class()
        print("=" * 16, end='')
        print("[강의 정보 열람]", end='')
        print("=" * 18)
        for classData in classInfo:
            for className in myClassList:
                if classData[0]==className:
                    print('★ ', end='')
            print('(' + classData[0] + ') '+classData[5].replace('@',' '))  #classID >> className
            print('강사 : ' + textManager.teacherID_to_teacherName(classData[1])) #teacherID >> teacherName
            print('연락처 : ' + textManager.teacherID_to_teacherPhone(classData[1]))
            print('강의실 : ' + classData[2])
            print('수업 시간 : '+ textManager.classID_to_classTime(classData[0], classData[2]) + '교시')  #classID >> classTime
            print('수용학생인원 : ' + textManager.roomID_to_roomMaxSeat(classData[2]) + '명')
            print('========================================')
        #메뉴
        print('1. 수강생 정보 확인')
        print('2. 뒤로가기')
        select = input('선택 : ') or '입력 실패'
        if select == '입력 실패':
            print("데이터 값을 입력해 주세요.")
            time.sleep(2)
            os.system('cls')
            continue
        elif rule.numberRule(select)==0:
            time.sleep(2)
            os.system('cls')
            continue
        select = int(select)
        if select==1:
            # 1번 시 학생이면 돌려내기
            if isTeacher==False:
                print('사용자는 해당 기능에 접근할 수 없습니다.')
                time.sleep(2)
                continue

            # 찾아볼 강의 선택 입력받기
            print('========================================')
            print('열람하실 강의의 고유 번호를 입력 해 주세요.')
            myClassCode=input('고유번호: ')
            print('========================================')
            find=False
            for className in myClassList:
                if myClassCode==className:
                    find=True
            if find==False:
                print('입력하신 강의가 찾을 수 없는 강의이거나, 개설하신 강의가 아닙니다.')
                time.sleep(2)
                continue

            # 수강생 목록 받기
            studentList = textManager.classID_to_studentList(myClassCode)
            while True:
                os.system('cls')
                print("=" * 16, end='')
                print("[수강생 정보 확인]", end='')
                print("=" * 18)
                print('('+myClassCode+')'+' 수강 학생 :') #classData 그냥 C4 뜨네요.. myClassCode교체
                for studentCode in studentList:
                    #전재원 (S21), 01017345312
                    #studentData = textManager.readText_Student_c(studentCode)
                    print(studentCode[1]+' ('+studentCode[0]+'), '+studentCode[2])
                print('========================================')
                print('1. 뒤로 가기')
                mySelect = input('') or '입력 실패'
                if mySelect == '입력 실패':
                    print("데이터 값을 입력해 주세요.")
                elif rule.numberRule(mySelect) == 0:
                    time.sleep(2)
                    os.system('cls')
                    continue
                mySelect=int(mySelect)
                if mySelect==1:
                    break
                else:
                    print('뒤로가려면 1을 입력하세요')
                    time.sleep(2)
                    continue

        elif select==2:
            # 뒤로가기
            os.system('cls')
            return
        else:
            print('잘못된 입력입니다. 다시 입력해주세요.')
            time.sleep(2)
            continue
