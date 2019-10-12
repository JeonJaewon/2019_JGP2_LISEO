import time
import os
import textManager

# 출력 함수 == 메인 함수
def myClass(code, classInfo, roomInfo, schedule):    # code : 해당 학생/선생 정보 배열    classInfo : 수업들의 코드가 담긴 배열, roomInfo : 강의실의 코드가 담긴 배열
        if "S" in code[0]:
            while 1:
                print("내가 수강하는 강의 :")
                # 해당 학생이 수강하는 강의 목록 출력
                studentInfo = textManager.readText_Student_c(code)  # 해당 학생의 정보를 저장해놓은 1차원 배열
                classArr = textManager.Re_UserInfo(code)
                for i in range(len(classArr)):               # --> 반복문이 실행될 때 마다 계속 불러오므로 Data갱신에 대한 걱정 안해도 됨
                    print("(" + classArr[i][0] + ") " + classArr[i][1])
                print("-------------------------------------------")
                print("\t1. 수강 신청")
                print("\t2. 수강 취소")
                print("\t3. 뒤로 가기")
                ans = int(input("원하는 항목 : "))
                os.system('cls')
                if ans == 1:
                    enrolement(classInfo,code)
                elif ans == 2:
                    cancelClass(classInfo,code)
                elif ans == 3:
                    return
                # 1,2,3을 제외한 이상한 답이 나왔을 경우는 다시 반복문 처음으로~~~
        else:
            while 1:
                print("내가 개설한 강의 :")
                # 해당 선생이 개설한 강의 목록 출력
                teacherInfo = textManager.readText_Teacher_c(code)  # 해당 선생의 정보를 저장해놓은 1차원 배열
                classArr = textManager.Re_UserInfo(code)
                for i in range(len(classArr)):               # --> 반복문이 실행될 때 마다 계속 불러오므로 Data갱신에 대한 걱정 안해도 됨
                    print("(" + classArr[i][0] + ") " + classArr[i][1])
                print("-------------------------------------------")
                print("\t1. 강의 개설")
                print("\t2. 강의 정보 수정")
                print("\t3. 강의 삭제")
                print("\t4. 뒤로 가기")
                ans = int(input("원하는 항목 : "))
                os.system('cls')
                if ans == 1:
                    makeClass()
                    # textManager.modify_Room("C5",5,"R5",0)
                elif ans == 2:
                    modifyClass(classInfo,roomInfo)
                elif ans == 3:
                    deleteClass(classInfo)
                elif ans == 4:
                    return
                # 1,2,3,4를 제외한 이상한 답이 나왔을 경우는 다시 반복문 처음으로~~~


def enrolement(classInfo,code):  # 수강 신청
    classCode = input("내가 수강하고 싶은 강의의 고유 번호를 입력하세요. : ")
    if classCode in classInfo:
        textManager.enrollOrCancelClass(classCode,code,0)
        #textManager.writeText_Class(code[0], classCode)    # Class.txt를 수정하는 텍스트 파일 --> classCode 추가
        print("수강 신청이 완료되었습니다.")
    else:
        print("존재하지 않은 고유 번호입니다.")
    time.sleep(2)
    os.system('cls')

def cancelClass(classInfo,code): # 수강 취소
    classCode = input("내가 수강 취소하고 싶은 강의의 고유 번호를 입력하세요. : ")
    if classCode in classInfo:
        textManager.enrollOrCancelClass(classCode,code,1)

        # Class.txt의 해당 강의 내용 수정 (듣는 인원 -1)
        print("수강 취소가 완료되었습니다.")
    else:
        print("존재하지 않은 고유 번호입니다.")
    time.sleep(2)
    os.system('cls')

def printSchedule():
    schedule=textManager.readText_Room()
    print("** 현재 강의 시간표 ** ")
    tempStr="  　　"
    for i in schedule[0]:
        tempStr+="\t"+i
    print(tempStr)
    print("----------------------------------------------")
    for i in range(1,len(schedule)):
        tempStr=str(i)+"교시"
        for Class in schedule[i]:
            tempStr+="\t"+Class
        print(tempStr)

def makeClass():  # 강의 개설
    printSchedule()     # 현재 강의 시간표 출력
    print("==============================================")
    className = input("내가 개설할 강의의 이름을 입력하세요. : ")
    classTime = input("내가 개설할 강의의 시간대를 입력하세요. (-교시) : ")
    # textManager.writeText_Class(className, classTime)
    # 고유번호도 자동생성되어야 할 듯
    # textManager.writeText_Teacher(classCode)  # 그리고 생성된 고유번호를 여기에다가 넣는거지
    # schedule[3][1]   == R1교실(교실 배열의 첫 번째 idx)에서 진행되는 3교시의 수업. 공란일 경우(0으로 정의하자) 수업 X, 강의 고유번호가 있을 경우 수업 이미 O.
    for i in range(1,len(roomInfo)):
        if schedule[classTime][i] == 0:
            # textManager.writeText_Class(classCode)
            # textManager.writeText_Room(classCode)    # 표 갱신
            print("성공적으로 강의가 개설되었습니다.")
            print("강의명 : "+className+", 시간 : "+classTime+"교시")
            break
        if i==len(roomInfo)-1:  # 교실 (열) 을 전부 돌았는 데도 빈 자리가 없을 경우
            print("해당 교시에 이미 강의가 있습니다.")
            break
    time.sleep(2)
    os.system('cls')

def modifyClass(classInfo, roomInfo): # 강의 정보 수정
    classCode=input("수정할 강의의 고유 번호를 입력하세요. : ")
    if classCode in classInfo:
        # className, teacher, classTime, classroom=textManager.writeText_Class(classCode)
        while 1:
            print("("+classCode+") "+"className" + "\n강사 : "+"teacher"+"\n교실 : " + "classroom" + "\n시간 : "+"classTime"+"교시")
            print("1. 강의명 수정")
            print("2. 교실 및 시간 변경")
            print("3. 뒤로 가기")
            ans=int(input("원하는 항목 : "))
            if ans==1:
                newName=input("className"+" >> ")
                # 여기에서 입력조건 검사도 들어가야겠죵?
                # textManager.writeText_Class(classCode)   # 정보 수정된 것 들어감
                # textManager.writeText_Room(classCode)    # 표 갱신
                print("정보가 성공적으로 수정되었습니다.")
                break

            elif ans==2:
                newRoom=input("classroom"+" >> ")
                if not newRoom in roomInfo:     # 새로 입력한 강의실이 현재 강의실 목록에 존재하지 않으면
                    print("존재하지 않는 강의실입니다.")
                    time.sleep(2)
                    os.system('cls')
                    continue
                # 새로 입력한 강의실이 현재 강의실 목록에 존재 할 경우
                # 정보 수정된 것 들어감
                # textManager.writeText_Class(classCode)
                # textManager.writeText_Room(classCode)    # 표 갱신
                print("정보가 성공적으로 수정되었습니다.")

                newTime=input("classTime"+" >> ")
                # if 숫자입력규칙 어긋남:
                #   print("존재하지 않는 시간대입니다.")
                # elif schedule[classTime][classroom] != 0:
                #    print("이미 등록된 강의실입니다.")
                # else: --> 정상적인 경우
                    # 정보 수정된 것 들어감
                    # textManager.writeText_Class(classCode)
                    # textManager.writeText_Room(classCode)    # 표 갱신
                    # print("정보가 성공적으로 수정되었습니다.")
                    # break

            elif ans==3:
                break
            time.sleep(2)   # 위의 ans case문 안에서 if로 걸러진 것들은 다 이 밑으로 내려가겠져? (존재하지 않는 강의실 경우 제외)
            os.system('cls')    # 그게 밑으로 내려가면 이렇게 딱! 화면이 지워지고 다시 while문의 처음으로 돌아간다 이말이야~

    else:
        print("존재하지 않은 고유 번호입니다.")
    time.sleep(2)
    os.system('cls')

def deleteClass(classInfo):
    classCode=input("삭제할 강의의 고유 번호를 입력하세요. : ")
    if classCode in classInfo:
        # textManager.writeText_Class(classCode)    --> 해당 강의가 속해있는 줄 모두 삭제ㅔ
        # --> 선생 정보 변경
        # textManager.writeText_Room(classCode)    # 표 갱신
        # 학생은... 학생이 수강하는 강의는 표시 안한다고 했으니까 없어두 되겠지?
        print("강의 삭제가 완료되었습니다.")
    else:
        print("존재하지 않은 고유 번호입니다.")