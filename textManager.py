def readText_Student():
    student = open("student.txt", 'r', encoding='UTF-8-SIG')
    StudentInfo = [] # 2차원 list 로 학생정보 저장
    i = 0
    while True:
        StudentData = student.readline() # student.txt 파일 읽기
        if not StudentData: # txt 마지막 줄에 도달하면 break
            return -1
        StudentLogin = StudentData.rstrip("\n").split(' ') # rstrip으로 개행문자 제거
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
            return -1
        StudentLogin = StudentData.rstrip("\n").split(' ')  # rstrip으로 개행문자 제거
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
        TeacherLogin = TeacherData.rstrip("\n").split(' ')# rstrip으로 개행문자 제거
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
        TeacherLogin = TeacherData.rstrip("\n").split(' ')# rstrip으로 개행문자 제거
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
        ClassLogin = ClassData.rstrip("\n").split(' ')# rstrip으로 개행문자 제거
        # 학생 정보만 따로 list에 담는 과정
        students = ClassLogin[6:]
        del (ClassLogin[6:])
        ClassInfo.append(ClassLogin)
        ClassInfo[i].append(students)
        i += 1
    Class.close()
    return ClassInfo # 강의 정보 반환

def readText_Class_c(code):   # 위에껀 전체, 이건 해당 고유번호 정보만 반환
    Class = open("class.txt", 'r', encoding='UTF-8-SIG')
    ClassInfo = [] # 3차원 list 로 강의정보 저장
    i = 0
    while True:
        ClassData = Class.readline()
        if not ClassData:
            break
        ClassLogin = ClassData.rstrip("\n").split(' ')# rstrip으로 개행문자 제거
        # 학생 정보만 따로 list에 담는 과정
        students = ClassLogin[6:]
        del (ClassLogin[6:])
        ClassInfo.append(ClassLogin)
        ClassInfo[i].append(students)
        if code == ClassInfo[i][0]: # txt돌면서 맞는 고유번호 확인
            Class.close()
            return ClassInfo[i] # 해당하는 정보만 반환
        i += 1

def readText_Room():
    room = open("room.txt", 'r', encoding='UTF-8-SIG')
    RoomInfo = [] # 2차원 list 로 장소정보 저장 (행 : 교시(0(방이름)~5, 열 : 교실))
    while True:
        RoomRow = room.readline()
        if not RoomRow:
            break
        RoomCol = RoomRow.rstrip("\n").split('@')# rstrip으로 개행문자 제거
        RoomInfo.append(RoomRow)
    room.close()
    return RoomInfo # 장소 정보 반환

###### classView.py에 필요하여 추가! by 계 #####
###### myClass.py에도 필요하여 더 추가! by 혜 #####
def classID_to_className(code):
    #class의 고유 번호 >> class의 이름
    classInfo=readText_Class_c(code)
    className=classInfo[5].replace("@"," ")     # 강의명의 @를 공백으로 수정
    return className

def teacherID_to_teacherName(code):
    #teacher의 고유번호 >> teacher의 이름 반환함수
    teacherData = readText_Teacher_c(code)
    return teacherData[1]

def teacherID_to_teacherPhone(code):
    #teacher의 고유번호 >> teacher의 이름 반환함수
    teacherData = readText_Teacher_c(code)
    return teacherData[2]

def classID_to_classTime(classCode, roomCode):
    #class의 고유번호, class의 강의교실 고유번호 >> class의 강의시간(교시) 반환함수
    roomInfo = readText_Room()
    roomCode=int(roomCode[1:])
    for j in range(1, 6):
        if roomInfo[roomCode-1][j]==classCode:
            return str(j)

def classID_to_studentList(classCode):
    #class의 고유번호 >> class의 수강학생 리스트 반환함수
    studentList=[]
    studentInfo = readText_Student()
    for studentData in studentInfo:
        for i in range(len(studentData[3])):
            if studentData[3][i]==classCode:
                studentList.append(studentData[0])
    return studentList
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
            newdata.append(ClassData.replace(' '+content, '')) # 고유번호 찾아서 빈칸으로 만듬
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
        codenum = int(code[1])+1  #코드 숫자 부분
        code = code[0] + str(codenum) #새로운 코드 생성
        newline = '\n'+ code + ' ' + number +' '+ content # 한 문장으로 합치기 number = 이름 content = 전화번호/공백으로 변경
        addstudent.write(newline) # 글 쓰기

########## myClass.py 전용 함수들 ##########
def deleteClassText(code):   # flag : 0(추가), 1(학생 삭제), 2(강의 삭제)
    classFile = open("classTest.txt", 'r', encoding='UTF-8-SIG')
    classLines = classFile.readlines() # 라인 전부 읽어오고
    if len(classLines) != 0:
        classLines[0] = classLines[0].replace(u"\ufeff", '')  # utf-8-sig로도 안없어져서 강제로 없앰
    classWrite = open("classTest.txt", 'w', encoding='UTF-8-SIG') # W로 오픈하면 텍스트 전부 삭제됨.

    for line in classLines:
        if code != line.split(' ')[0]: # code랑 저장해놨던 line들의 코드랑 비교해서
            classWrite.write(line) # 같지 않으면, 즉 삭제할려고 했던게 아니면 다시 써준다

def enrollOrCancelClass(classCode,studentCode, flag):  # flag : 0(수강 신청), 1(수강 취소)
    classFile = open("classTest.txt", 'r', encoding='UTF-8-SIG')
    classLines = classFile.readlines()
    if len(classLines) != 0:
        classLines[0] = classLines[0].replace(u"\ufeff", '')  # utf-8-sig로도 안없어져서 강제로 없앰
    classWrite = open("classTest.txt", 'w', encoding='UTF-8-SIG')



    if flag == 0:
        for line in classLines:
            if classCode != line.split(' ')[0]:
                classWrite.write(line)
    elif flag == 1:
        for line in classLines:
            if classCode!= line.split(' ')[0]:
                classWrite.write(line)
