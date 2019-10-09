def readText_Student():
    student = open("student.txt", 'r', encoding='UTF-8')
    StudentInfo = [] # 2차원 list 로 학생정보 저장
    i = 0
    while True:
        StudentData = student.readline()
        if not StudentData:
            break
        StudentLogin = StudentData.split(',')
        lecture = StudentLogin[3:] # 강의 정보들 따로 list
        del(StudentLogin[3:]) # 강의 정보들 str 삭제
        StudentInfo.append(StudentLogin)
        StudentInfo[i].append(lecture)
        i += 1

def readText_Teacher():
    teacher = open("teacher.txt", 'r', encoding='UTF-8')
    TeacherInfo = [] # 2차원 list 로 선생정보 저장
    i = 0
    while True:
        TeacherData = teacher.readline()
        if not TeacherData:
            break
        TeacherLogin = TeacherData.split(',')
        lecture = TeacherLogin[3:]
        del(TeacherLogin[3:])
        TeacherInfo.append(TeacherLogin)
        TeacherInfo[i].append(lecture)
        i += 1

def readText__Class():
    Class = open("class.txt", 'r', encoding='UTF-8')
    ClassInfo = [] # 2차원 list 로 강의정보 저장
    while True:
        ClassData = Class.readline()
        if not ClassData:
            break
        ClassLogin = ClassData.split(',')
        ClassInfo.append(ClassLogin)

def readText_Room():
    room = open("room.txt", 'r', encoding='UTF-8')
    RoomInfo = [] # 2차원 list 로 장소정보 저장
    while True:
        RoomData = room.readline()
        if not RoomData:
            break
        RoomLogin = RoomData.split(',')
        RoomInfo.append(RoomLogin)

def writeText_Student():
    student = open("student.txt", 'w', encoding='UTF-8')

def writeText_Teacher():
    teacher = open("teacher.txt", 'w', encoding='UTF-8')

def writeText_Class():
    classroom = open("class.txt", 'w', encoding='UTF-8')

def writeText_Room():
    room = open("room.txt", 'w', encoding='UTF-8')
