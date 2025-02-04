﻿#-*- coding: utf-8 -*-
def readText_Student():
    student = open("student.txt", 'r', encoding='UTF-8-SIG')
    StudentInfo = [] # 2차원 list 로 학생정보 저장
    i = 0
    while True:
        StudentData = student.readline() # student.txt 파일 읽기
        if not StudentData: # txt 마지막 줄에 도달하면 break
            break # ㅂㄷㅂㄷ...
        StudentLogin = StudentData.rstrip("\n").split('@') # rstrip으로 개행문자 제거
        # lecture = StudentLogin[3:] # 강의 정보들 따로 list`` # StudentLogin : 강의 정보 저장 위해 임시로 만든 배열
        # del(StudentLogin[3:]) # 강의 정보들 str 삭제
        StudentInfo.append(StudentLogin) # 학생 정보 저장
        # StudentInfo[i].append(lecture) # 강의 정보 저장
        # i += 1
    student.close()
    return StudentInfo # 학생 정보 반환

# 고유 번호 확인용(학생)
def readText_Student_c(code):
    student = open("student.txt", 'r', encoding='UTF-8-SIG')
    StudentInfo = []  # 2차원 list 로 학생정보 저장
    i = 0
    while True:
        StudentData = student.readline()  # student.txt 파일 읽기

        if not StudentData:  # txt 마지막 줄에 도달하면 break
            break # ㅂㄷㅂㄷ...
        StudentLogin = StudentData.rstrip("\n").split('@')  # rstrip으로 개행문자 제거
        # lecture = StudentLogin[3:]  # 강의 정보들 따로 list
        # del (StudentLogin[3:])  # 강의 정보들 str 삭제
        StudentInfo.append(StudentLogin)  # 학생 정보 저장
       #  StudentInfo[i].append(lecture)  # 강의 정보 저장
        #print(StudentInfo[i][0]) #test 용도로 출력하는거 같아서 주석처리! ( by 계 )
        if code == StudentInfo[i][0]: # 맞는 고유번호 확인
            student.close()
            return StudentInfo[i] # 해당하는 정보만 반환(1차원배열)
        i += 1

def readText_Teacher():
    teacher = open("teacher.txt", 'r', encoding='UTF-8-SIG')
    TeacherInfo = [] # 2차원 list 로 선생정보 저장
    i = 0
    while True:
        TeacherData = teacher.readline()
        if not TeacherData:
            break
        TeacherLogin = TeacherData.rstrip("\n").split('@')# rstrip으로 개행문자 제거
        lecture = TeacherLogin[3:]
        # del(TeacherLogin[3:])
        TeacherInfo.append(TeacherLogin)
        # TeacherInfo[i].append(lecture)
        # i += 1
    teacher.close()
    return TeacherInfo # 선생님 정보 반환

#고유 번호 확인용(선생님)
def readText_Teacher_c(code):
    teacher = open("teacher.txt", 'r', encoding='UTF-8-SIG')
    TeacherInfo = [] # 2차원 list 로 선생정보 저장
    i = 0
    while True:
        TeacherData = teacher.readline()
        if not TeacherData:
            break
        TeacherLogin = TeacherData.rstrip("\n").split('@')# rstrip으로 개행문자 제거
        # lecture = TeacherLogin[3:]
        del(TeacherLogin[3:])
        TeacherInfo.append(TeacherLogin)
        # TeacherInfo[i].append(lecture)
        if code == TeacherInfo[i][0]: # txt돌면서 맞는 고유번호 확인
            teacher.close()
            return TeacherInfo[i] # 해당하는 정보만 반환
        i += 1

def readText_Class():   # 굳이 언더바가 두 개일 필요는 없어서 고쳤습니다. -혲니
    Class = open("class.txt", 'r', encoding='UTF-8-SIG')
    ClassInfo = [] # 3차원 list 로 강의정보 저장
    i = 0
    while True:
        ClassData = Class.readline()
        if not ClassData:
            break
        ClassLogin = ClassData.rstrip("\n").split('@')# rstrip으로 개행문자 제거
        # 학생 정보만 따로 list에 담는 과정
        students = ClassLogin[6:]
        del (ClassLogin[6:])
        ClassInfo.append(ClassLogin)
        ClassInfo[i].append(students)
        i += 1
    Class.close()
    return ClassInfo # 강의 정보 반환

def readText_Class_ttoc(code):   #선생고유번호 넣었을 때 본인 강의 고유번호 리턴
    Class = open("class.txt", 'r', encoding='UTF-8-SIG')
    Classcode=[] #readText_Class_ttoc1차원 저장
    i = 0
    while True:
        ClassData = Class.readline()
        if not ClassData:
            break
        ClassLogin = ClassData.rstrip("\n").split('@')  # rstrip으로 개행문자 제거
        if code==ClassLogin[1]:
            Classcode.append(ClassLogin[0])
        i += 1
    Class.close()
    return Classcode #본인 강의고유번호배열 반환

def readText_Class_c(code):   # 위에껀 전체, 이건 해당 고유번호 정보만 반환
    Class = open("class.txt", 'r', encoding='UTF-8-SIG')
    ClassInfo = [] # 3차원 list 로 강의정보 저장
    i = 0
    while True:
        ClassData = Class.readline()
        if not ClassData:
            break
        ClassLogin = ClassData.rstrip("\n").split('@')# rstrip으로 개행문자 제거
        # 학생 정보만 따로 list에 담는 과정
        students = ClassLogin[6:]
        del (ClassLogin[6:])
        ClassInfo.append(ClassLogin)
        ClassInfo[i].append(students)
        if code == ClassInfo[i][0]: # txt돌면서 맞는 고유번호 확인
            Class.close()
            return ClassInfo[i] # 해당하는 정보만 반환
        i += 1

def readText_ClassCode():   # 수업의 고유번호만 모아놓은 배열
    ClassInfo=readText_Class()
    classCodeArr = []
    for i in range(len(ClassInfo)):
        classCodeArr.append(ClassInfo[i][0])
    return classCodeArr

def readText_Class_stoc(code):   # 학생코드치면 수업고유번호 반환
    Class = open("class.txt", 'r', encoding='UTF-8-SIG')
    ClassInfo = [] # 1차원저장
    i = 0
    while True:
        ClassData = Class.readline()
        if not ClassData:
            break
        ClassLogin = ClassData.rstrip("\n").split('@')# rstrip으로 개행문자 제거
        # 학생 정보만 따로 list에 담는 과정
        students = ClassLogin[6:]
        if code in students:
            ClassInfo.append(ClassLogin[0])
        i += 1
    Class.close()
    return ClassInfo


def readText_Room():
    room = open("room.txt", 'r', encoding='UTF-8-SIG')
    RoomInfo = [] # 2차원 list 로 장소정보 저장 (행 : 교시(0(방이름)~5, 열 : 교실))
    while True:
        RoomRow = room.readline()
        if not RoomRow:
            break
        RoomCol = RoomRow.rstrip("\n").split('@')# rstrip으로 개행문자 제거
        RoomInfo.append(RoomCol)
#    for j, roomName in enumerate(RoomInfo[0]):
#        for i,tempStr in enumerate(roomName):
#            if tempStr.replace("u\ufeff", '')==",":     # ,나오기 전까지 자르기
#                RoomInfo[0][j]=RoomInfo[0][j][:i]
#                break
    room.close()
    return RoomInfo # 장소 정보 반환

def readText_RoomName():    # 강의실 이름 정보만 반환
    room = open("room.txt", 'r', encoding='UTF-8-SIG')
    RoomRow = room.readline()
    if not RoomRow:
        return -1
    RoomCol = RoomRow.rstrip("\n").split('@')# rstrip으로 개행문자 제거
    for j, roomName in enumerate(RoomCol):
        for i,tempStr in enumerate(roomName):
            if tempStr.replace("u\ufeff", '')==",":     # ,나오기 전까지 자르기
                # roomName=roomName[:i-1] --> 이건 값 수정이 안되는군요.
                RoomCol[j]=RoomCol[j][:i]
                break
    room.close()
    return RoomCol # 장소 정보 반환

def readText_RoomMaxNum():  # 강의실 최대 수용 인원 정보 반환 (강의실 이름 정보 반환하는 1차원 배열과 일대일 대응)
    room = open("room.txt", 'r', encoding='UTF-8-SIG')
    RoomRow = room.readline()
    if not RoomRow:
        return -1
    RoomCol = RoomRow.rstrip("\n").split('@')# rstrip으로 개행문자 제거
    for j,roomName in enumerate(RoomCol):
        for i,tempStr in enumerate(roomName):
            if tempStr.replace("u\ufeff", '')==",":     # ,나오기 전까지 자르기
                # roomName=roomName[i+1:] --> 이건 값 수정이 안되는군요.
                RoomCol[j]=RoomCol[j][i+1:]
                break
    room.close()
    return RoomCol

###### classView.py에 필요하여 추가! by 계 #####
###### myClass.py에도 필요하여 더 추가! by 혜 #####
def classID_to_className(code):
    #class의 고유 번호 >> class의 이름
    classInfo=readText_Class_c(code)
    className=classInfo[5]  #.replace("@"," ")     # 강의명의 @를 공백으로 수정
    return className

def teacherID_to_teacherName(code):
    #teacher의 고유번호 >> teacher의 이름 반환함수
    teacherData = readText_Teacher_c(code)
    return teacherData[1]

def teacherID_to_teacherPhone(code):
    #teacher의 고유번호 >> teacher의 이름 반환함수
    teacherData = readText_Teacher_c(code)
    return teacherData[2]

def roomID_to_roomMaxSeat(roomCode):
    #room의 고유번호  >>  room의 최대수용인원
    roomInfo = open("roomInfo.txt",'r', encoding='UTF-8-SIG')
    for roomData in roomInfo:
        roomData = roomData.split('@')
        if roomData[0]==roomCode:
            return str(int(roomData[1]))

def classID_to_classTime(classCode, roomCode):
    #class의 고유번호, class의 강의교실 고유번호 >> class의 강의시간(교시) 반환함수
    roomInfo = readText_Room()
    roomCode=int(roomCode[1:])
    for j in range(1, 6):
        if roomInfo[j][roomCode-1]==classCode:
            return str(j)

def classID_to_studentList(classCode):
    #class의 고유번호 >> class의 수강학생 리스트 반환함수
    #studentInfo = readText_Student()
    whostudent = [] #어떤 학생이 이 강의를 듣는가?
    classInfo = readText_Class() # 이젠 student.txt에 없음
    #범위가 바뀌고 여기를 바꿔야 되고
    i = 0
    while i < len(classInfo):
        if classCode == classInfo[i][0]:
            j = 0
            while j < len(classInfo[i][6]):
                studentInfo = readText_Student_c(classInfo[i][6][j])
                whostudent.append(studentInfo)
                j += 1
        i += 1
    return whostudent
###################################################

##### 1. 마이페이지 함수 들 ######
def Re_UserInfo(code):   # myClass.py와 같이 쓰기 위해 출력함수 대신 강의 고유코드와 이름을 저장하는 배열을 반환하는 걸로 바꿈
    Class = open("class.txt", 'r', encoding='UTF-8-SIG')
    Classname = readText_Class()
    where = []
    i = 0
    while True:
        ClassData = Class.readline()
        if not ClassData:
            break
        if ClassData.find(code) != -1: # -1이 아니면 code가 존재한다는 것
            where.append(i) # where list에 저장!
        i += 1
    i = 0
    classArr = []  # [][ 학생/선생이 수강/개설한 강의의 고유 번호, 강의명 ]
    for i in where:
        classArrCol = []  # [ 학생/선생이 수강/개설한 강의의 고유 번호, 강의명 ]
        classArrCol.append(Classname[i][0])    # 강의 고유 번호 저장
        classArrCol.append(Classname[i][5])    # 강의 이름 저장
        classArr.append(classArrCol)
    Class.close()
    return classArr


def RenewalName(code,oldname,newname):
    newdata = []
    if code[0] == 'S': # 학생일 때
        student = open("student.txt", 'r', encoding='UTF-8-SIG')
        while True:
            StudentData = student.readline()  # student.txt 파일 읽기
            if not StudentData:  # txt 마지막 줄에 도달하면 break
                break
            newdata.append(StudentData.replace(oldname, newname)) # 수정
        i = 0
        student.close()
        writestudent = open("student.txt", 'w', encoding='UTF-8-SIG')
        i = 0
        while i < len(newdata):
            writestudent.write(newdata[i])  # student.txt 쓰기
            i += 1
        writestudent.close()
    else: #선생님 일때
        teacher = open("teacher.txt", 'r', encoding='UTF-8-SIG')
        while True:
            TeacherData = teacher.readline()
            if not TeacherData:
                break
            newdata.append(TeacherData.replace(oldname, newname)) # 수정
        i = 0
        teacher.close()
        writeteacher = open("teacher.txt", 'w', encoding='UTF-8-SIG')
        i = 0
        while i < len(newdata):
            writeteacher.write(newdata[i])  # teacher.txt 쓰기
            i += 1
        writeteacher.close()

def Re_StuClass():
    student = open("student.txt", 'w', encoding='UTF-8-SIG')
    teacher = open("teacher.txt", 'w', encoding='UTF-8-SIG')
    Class = open("class.txt", 'w', encoding='UTF-8-SIG')
    room = open("room.txt", 'w', encoding='UTF-8-SIG')


def Re_TeaClass():
    student = open("student.txt", 'w', encoding='UTF-8-SIG')
    teacher = open("teacher.txt", 'w', encoding='UTF-8-SIG')
    Class = open("class.txt", 'w', encoding='UTF-8-SIG')
    room = open("room.txt", 'w', encoding='UTF-8-SIG')


def Re_Student(number,content):
    student = readText_Student()
    if number == '1': # 이쪽은 학생 정보 삭제 content = 고유번호
        # 몇번째줄 지워야 되는지 체크
        i = 0
        re_line = -1 # re_line 값이 없을 수도 있어서 -1 대입
        while i < len(student):
            if content == student[i][0]:  # 맞는 고유번호인지 확인
                re_line = i  # 몇번 째줄 지워야 하는지 확인
                break
            i += 1
        # 찾는 코드가 없으면?
        if re_line == -1: # re_line 값이 안바꼈으니까
            return -1 # 틀렸다고 -1 반환
        newline = []
        read_s = open("student.txt", 'r', encoding='UTF-8-SIG')
        # list안에 str로 한줄 씩 받기
        while True:
            StudentData = read_s.readline()  # student.txt 파일 읽기
            newline.append(StudentData) #list에 str 형태로 저장
            if not StudentData:  # txt 마지막 줄에 도달하면 break
                break
            elif StudentData == '\n': #txt에 띄어쓰기 된거 제거
                break
        del newline[re_line] # newline 값이 없을 수도 있음/ 해당 줄 삭제
        read_s.close()
        # txt 초기화 후 다시 쓰기
        write_s = open("student.txt", 'w', encoding='UTF-8-SIG') # student.txt 초기화
        i = 0
        while i < len(newline):
            write_s.write(str(newline[i])) # student.txt 쓰기
            i += 1
        write_s.close()
        # class.txt 저장되어 있는 학생 정보 지우기
        readclass = open("class.txt", 'r', encoding='UTF-8-SIG')
        newdata = []
        while True:
            ClassData = readclass.readline()
            if not ClassData:
                break
            newdata.append(ClassData.replace('@'+content, '')) # 고유번호 찾아서 빈칸으로 만듬
        readclass.close()
        writeclass = open("class.txt", 'w', encoding='UTF-8-SIG')
        i = 0
        while i < len(newdata):
            writeclass.write(newdata[i])  # class.txt 쓰기
            i += 1
        writeclass.close()


    #몇 줄인지 확인후 코드 생성 -> 마지막 코드 번호 확인후 +1된 코드 생성
    else: #이쪽은 학생 정보 추가
        addstudent = open("student.txt", 'a+', encoding='UTF-8-SIG')  # txt 문장 추가
        code = student[len(student)-1][0] # 코드 전체 부분
        codenum = int(code[1:])+1  #코드 숫자 부분
        code = code[0] + str(codenum) #새로운 코드 생성
        newline = code + '@' + number +'@'+ content+'\n' # 한 문장으로 합치기 number = 이름 content = 전화번호/공백으로 변경
        addstudent.write(newline) # 글 쓰기


########## myClass.py 전용 함수들 ##########
def modify_Class(code, flag):   # flag : 0(추가), 1(삭제)
    add = open("class.txt", 'a+', encoding='UTF-8-SIG')


def modify_Room(classCode, time, room, flag):    # flag : 0(추가), 1(삭제)
    roomInfo=readText_Room()
    # print(roomInfo)
    roomNum=int(room[1:])   # 강의실 코드(R1,..)에서 숫자 부분만 자름
    if flag==0:
            roomInfo[int(time)][roomNum-1] = classCode
    elif flag==1:
        roomInfo[int(time)][roomNum - 1] = "N"
    else:
        return -1

    data=""
    for i in range(len(roomInfo)):
        for roomData in roomInfo[i]:
            data+=roomData+"@"
        data=data.rstrip('@')    # 위의 반복문대로 하면 맨 오름쪽에 @가 남는데, 그걸 없애고 개행 문자를 추가함
        data+="\n"
    wf = open("room.txt", 'w', encoding='UTF-8-SIG')
    wf.write(data)
    wf.close()

def modify_ClassInfo(classCode,newName,newTime,newRoom): # 강의실 정보 수정 함수. 인자에 -1이 들어가지 않은 것만 고침
    Class=readText_Class_c(classCode)
    if newName == -1:
        newName = Class[5]
    if newTime == -1:
        newTime = Class[4]
    if newRoom == -1:
        newRoom = Class[2]
#    idx=int(classCode[1:])-1    # 해당 고유 번호가 전체 강의 목록 3차원 배열에서 몇 층인지
    if newName != -1:
        Class[5] = newName
    if newTime != -1:
        Class[4] = newTime
    if newRoom != -1:
        Class[2] = newRoom
    idx=int(classCode[1:])-1    # 해당 고유 번호가 전체 강의 목록 3차원 배열에서 몇 층인지
    classArr=readText_Class()
#    classArr[idx]=Class

    dataArr=[]
    for i in range(len(classArr)):
        if classCode==classArr[i][0]:
            data=classArr[i][0]+"@"+classArr[i][1]+"@"+newRoom+"@"+classArr[i][3]+"@"+str(newTime)+"@"+newName+"@"
            if classArr[i][6]:
                for students in classArr[i][6]:
                    data+=students+"@"
            data=data.rstrip("@")
            dataArr.append(data)
            continue
        data=""
        for j in range(6):  # 강의명까지(수강생 목록 전까지) 입력
           data+=str(classArr[i][j])+"@"
        if classArr[i][6]:  # 수강생이 있는지 없는지 확인
            for students in classArr[i][6]:
                data+=students+"@"
        data=data.rstrip('@')
        dataArr.append(data)
    wf = open("class.txt", 'w', encoding='UTF-8-SIG')
    for i in range(len(dataArr)):
        if i!=0:
            wf.write('\n')
        wf.write(dataArr[i])
    wf.close()


######## myClass.py 전용 추가 함수 ####### by 계
#class.txt에 새로 개설한 강의 추가 함수
def deleteClassText(code):
    classFile = open("class.txt", 'r', encoding='UTF-8-SIG')
    classLines = classFile.readlines() # 라인 전부 읽어오고
    if len(classLines) != 0:
        classLines[0] = classLines[0].replace(u"\ufeff", '')  # utf-8-sig로도 안없어져서 강제로 없앰
    classWrite = open("class.txt", 'w', encoding='UTF-8-SIG') # W로 오픈하면 텍스트 전부 삭제됨.

    fstFlag=0 #classCode에 첫번쨰 문장이 들어가면 1로 바뀜
    for line in classLines:
        if code != line.split('@')[0]: # code랑 저장해놨던 line들의 코드랑 비교해서
            if(fstFlag!=0):
                classWrite.write('\n')
            else:
                fstFlag=1
            classWrite.write(line[:-1]) # 같지 않으면, 즉 삭제할려고 했던게 아니면 다시 써준다
    classFile.close()
    classWrite.close()

def enrollOrCancelClass(classCode,studentCode, flag):  # flag : 0(수강 신청), 1(수강 취소)
    classFile = open("class.txt", 'r', encoding='UTF-8-SIG')
    classLines = classFile.readlines() # 모든 line 정보를 미리 classLines에 넣어둡니다
    if len(classLines) != 0:
        classLines[0] = classLines[0].replace("u\ufeff", '')  # utf-8-sig로도 안없어져서 강제로 없앰
    classWrite = open("class.txt", 'w', encoding='UTF-8-SIG') # w로 open 하면서 class.txt는 다 사라집니다

    if flag == 0: #수강신청
        for line in classLines: # 위에서 저장했던 classLine를 반복
            if classCode == line.split('@')[0]: # 내가 입력한 강의와 고유번호가 같다면
                strToList = line.rstrip("\n").split('@')
                studentStrList = strToList[6:]
                if studentCode in studentStrList: # 이미 수강중인 강의일때
                    classWrite.write(line)
                    print("이미 수강중인 강의입니다.")
                else:
                    classWrite.write(line.rstrip("\n")+'@'+studentCode+"\n") # 내 번호를 붙이고 다시 써준다
                    print("수강 신청이 완료되었습니다.")
            else:
                classWrite.write(line) # 아니면 원래 입력 그대로
    elif flag == 1: #수강취소
        for line in classLines:
            if classCode == line.split('@')[0]: # 내가 입력한 강의라면
                strToList = line.rstrip("\n").split('@')
                studentStrList = strToList[6:]  # 수강중 학생들 고유번호를 리스트로 받음. 6으로 하드코딩.txt파일 양식 변경시 수정할것.
                if studentCode not in studentStrList: # 수강중인 강의가 아니라면
                    classWrite.write(line)
                    print("수강중인 강의가 아닙니다.")
                else:
                    studentStrList.remove(studentCode) # 리스트에서 내 학번을 제거하고
                    newLine = '@'.join(strToList[:6])
                    newLine = newLine + '@' +'@'.join(studentStrList)+"\n" # 내 학번을 합친 문자열을 새로 넣어줌
                    classWrite.write(newLine)
                    print("수강 취소가 완료되었습니다.")
            else:
                classWrite.write(line)
    classFile.close()
    classWrite.close()

######## 강의 개설시 class.txt에 write하는 함수 ####### by 계
def add_class(teacherCode, roomCode, classTime, maxSeat, className):
    #class.txt에 내용 추가
    writeClass = open('class.txt', 'a+', encoding='UTF-8-SIG')
    readClass = readText_Class()
    classCode = 'C'+str(int(readClass[len(readClass)-1][0][1:])+1)
    # class.txt 양식 : 강의고유번호 선생고유번호 강의실고유번호 최대수용인원수 교시 이름 수강학생들
    inputString = '\n'+classCode+'@'+teacherCode+'@'+roomCode+'@'+str(maxSeat)+'@'+str(classTime)+'@'+className
    writeClass.write(inputString)
    writeClass.close()
    return classCode

##### studentManager.py 전용 함수 ####### by 계
# studentID >>> 수강중인 강의목록
def studentID_to_classList(studentCode):
    classInfo = readText_Class()
    classList=[]
    for classData in classInfo:
        for code in classData[6]:
            if code==studentCode:
                classList.append(classData[0])
    return classList

# PPT 4.3 빈 강의실 먼저 확인 하는 함수
def checkEmptyRoom(code):
    room = readText_Room() #room.txt 정보
    for i in [1,2,3,4,5]:
        if room[i][code-1] == 'N':
            return 1
    return 0
