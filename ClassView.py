import os
import textManager

def start(myID):
    #사용자의 권한 확인
    if(myID[0] == 'S'):
        #학생입니다.
        isTeacher = False
    elif(myID[0] == 'T'):
        # 선생님입니다.
        isTeacher = True
    else:
        print('error : 사용자의 ID 형식이 올바르지 않습니다.')
        return
    myClassList=[]
    if isTeacher:
        #자신의 개설강의 저장
        teacherData = textManager.readText_Teacher_c(myID)
        for i in range(len(teacherData)-3):
            myClassList.append(teacherData[i+3])
    else:
        #자신의 수강강의 저장
        studentData = textManager.readText_Student_c(myID)
        for i in range(len(studentData)-3):
            myClassList.append(studentData[i+3])

    #메인메뉴
    while True:
        # 모든 강의정보 출력 ( 자신의 수강 or 개설강의 별표로 표시)
        os.system('cls')
        classInfo = textManager.readText__Class()
        print('========================================')
        for classData in classInfo:
            for className in myClassList[0]:
                if classData[0]==className:
                    print('★ ', end='')
            print('(' + classData[0] + ') '+classData[5].replace('@',' '))  #classID >> className
            print('강사 : ' + textManager.teacherID_to_teacherName(classData[1])) #teacherID >> teacherName
            print('연락처 : ' + textManager.teacherID_to_teacherPhone(classData[1]))
            print('강의실 : ' + classData[2])
            print('수업 시간 : '+ textManager.classID_to_classTime(classData[0], classData[2]) + '교시')  #classID >> classTime
            print('수용학생인원 : ' + classData[3] + '명')
            print('========================================')
        #메뉴
        print('1. 수강생 정보 확인')
        print('2. 뒤로가기')
        select = int(input('선택 : '))
        if select==1:
            # 1번 시 학생이면 돌려내기
            if isTeacher==False:
                print('사용자는 해당 기능에 접근할 수 없습니다.')
                continue

            # 찾아볼 강의 선택 입력받기
            print('========================================')
            print('열람하실 강의의 고유 번호를 입력 해 주세요.')
            myClassCode=input('고유번호: ')
            print('========================================')
            find=False
            for className in myClassList[0]:
                if myClassCode==className:
                    find=True
            if find==False:
                print('입력하신 강의가 찾을 수 없는 강의이거나, 개설하신 강의가 아닙니다.')
                continue

            # 수강생 목록 받기
            textManager.classID_to_studentList(myClassCode)
            studentList = textManager.classID_to_studentList(myClassCode)
            while True:
                print('========================================')
                print('('+myClassCode+')'+' 수강 학생 :') #classData 그냥 C4 뜨네요.. myClassCode교체
                for studentCode in studentList:
                    #전재원 (S21), 01017345312
                    studentData = textManager.readText_Student_c(studentCode)
                    print(studentData[1]+' ('+studentData[0]+'), '+studentData[2])
                print('========================================')
                print('1. 뒤로 가기')
                mySelect = int(input(''))
                if mySelect==1:
                    break
                else:
                    print('뒤로가려면 1을 입력하세요')
                    continue

        elif select==2:
            # 2번 시 return 시키기
            print('뒤로가기입니다.')
            return
        else:
            print('잘못된 입력입니다. 다시 입력해주세요.')
            continue