def readText_Student():
    student = open("student.txt", 'r', encoding='UTF-8')
    StudentInfo = [] # 2차원 list 로 학생정보 저장
    i = 0
    while True:
        StudentData = student.readline() # student.txt 파일 읽기
        if not StudentData: # txt 마지막 줄에 도달하면 break
            break
        StudentLogin = StudentData.rstrip("\n").split(',') # rstrip으로 개행문자 제거
        lecture = StudentLogin[3:] # 강의 정보들 따로 list
        del(StudentLogin[3:]) # 강의 정보들 str 삭제
        StudentInfo.append(StudentLogin) # 학생 정보 저장
        StudentInfo[i].append(lecture) # 강의 정보 저장
        i += 1
    return StudentInfo # 학생 정보 반환

# 고유 번호 확인용(학생)
def readText_Student(code):
    student = open("student.txt", 'r', encoding='UTF-8')
    StudentInfo = []  # 2차원 list 로 학생정보 저장
    i = 0
    while True:
        StudentData = student.readline()  # student.txt 파일 읽기
        if not StudentData:  # txt 마지막 줄에 도달하면 break
            break
        StudentLogin = StudentData.rstrip("\n").split(',')  # rstrip으로 개행문자 제거
        lecture = StudentLogin[3:]  # 강의 정보들 따로 list
        del (StudentLogin[3:])  # 강의 정보들 str 삭제
        StudentInfo.append(StudentLogin)  # 학생 정보 저장
        StudentInfo[i].append(lecture)  # 강의 정보 저장
        if code == StudentInfo[i][0]: # 맞는 고유번호 확인
            return StudentInfo[i] # 해당하는 정보만 반환
        i += 1

def readText_Teacher():
    teacher = open("teacher.txt", 'r', encoding='UTF-8')
    TeacherInfo = [] # 2차원 list 로 선생정보 저장
    i = 0
    while True:
        TeacherData = teacher.readline()
        if not TeacherData:
            break
        TeacherLogin = TeacherData.rstrip("\n").split(',')# rstrip으로 개행문자 제거
        lecture = TeacherLogin[3:]
        del(TeacherLogin[3:])
        TeacherInfo.append(TeacherLogin)
        TeacherInfo[i].append(lecture)
        i += 1
    return TeacherInfo # 선생님 정보 반환

#고유 번호 확인용(선생님)
def readText_Teacher(code):
    teacher = open("teacher.txt", 'r', encoding='UTF-8')
    TeacherInfo = [] # 2차원 list 로 선생정보 저장
    i = 0
    while True:
        TeacherData = teacher.readline()
        if not TeacherData:
            break
        TeacherLogin = TeacherData.rstrip("\n").split(',')# rstrip으로 개행문자 제거
        lecture = TeacherLogin[3:]
        del(TeacherLogin[3:])
        TeacherInfo.append(TeacherLogin)
        TeacherInfo[i].append(lecture)
        if code == TeacherInfo[i][0]: # txt돌면서 맞는 고유번호 확인
            return TeacherInfo[i] # 해당하는 정보만 반환
        i += 1

def readText__Class():
    Class = open("class.txt", 'r', encoding='UTF-8')
    ClassInfo = [] # 2차원 list 로 강의정보 저장
    while True:
        ClassData = Class.readline()
        if not ClassData:
            break
        ClassLogin = ClassData.rstrip("\n").split(',')# rstrip으로 개행문자 제거
        ClassInfo.append(ClassLogin)
    return ClassInfo # 강의 정보 반환

def readText_Room():
    room = open("room.txt", 'r', encoding='UTF-8')
    RoomInfo = [] # 2차원 list 로 장소정보 저장
    while True:
        RoomData = room.readline()
        if not RoomData:
            break
        RoomLogin = RoomData.rstrip("\n").split(',')# rstrip으로 개행문자 제거
        RoomInfo.append(RoomLogin)
    return RoomInfo # 장소 정보 반환

def writeText_Student():
    student = open("student.txt", 'w', encoding='UTF-8')

def writeText_Teacher():
    teacher = open("teacher.txt", 'w', encoding='UTF-8')

def writeText_Class():
    classroom = open("class.txt", 'w', encoding='UTF-8')

def writeText_Room():
    room = open("room.txt", 'w', encoding='UTF-8')
