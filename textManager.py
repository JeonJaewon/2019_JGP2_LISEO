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



def Re_UserInfo():
    student = open("student.txt", 'w', encoding='UTF-8')
    teacher = open("teacher.txt", 'w', encoding='UTF-8')

def Re_StuClass():
    student = open("student.txt", 'w', encoding='UTF-8')
    teacher = open("teacher.txt", 'w', encoding='UTF-8')
    Class = open("class.txt", 'w', encoding='UTF-8')
    room = open("room.txt", 'w', encoding='UTF-8')


def Re_TeaClass():
    student = open("student.txt", 'w', encoding='UTF-8')
    teacher = open("teacher.txt", 'w', encoding='UTF-8')
    Class = open("class.txt", 'w', encoding='UTF-8')
    room = open("room.txt", 'w', encoding='UTF-8')


def Re_Student(number,content):
    student = readText_Student()
    if number == 1: # 이쪽은 학생 정보 삭제 content = 고유번호
        # 몇번째줄 지워야 되는지 체크
        i = 0
        re_line = -1 # re_line 값이 없을 수도 있음
        while i < len(student):
            if content == student[i][0]:  # 맞는 고유번호인지 확인
                re_line = i  # 몇번 째줄 지워야 하는지 확인
                break
            i += 1
        r_list = []
        read_s = open("student.txt", 'r', encoding='UTF-8')
        # list안에 str로 한줄 씩 받기
        while True:
            StudentData = read_s.readline()  # student.txt 파일 읽기
            r_list.append(StudentData) #list에 str 형태로 저장
            if not StudentData:  # txt 마지막 줄에 도달하면 break
                break
        del r_list[re_line] # re_line 값이 없을 수도 있음/ 해당 줄 삭제
        # txt 초기화 후 다시 쓰기
        write_s = open("student.txt", 'w', encoding='UTF-8') # student.txt 초기화
        i = 0
        while i < len(r_list):
            write_s.write(str(r_list[i])) # student.txt 쓰기
            i += 1


    else: #이쪽은 학생 정보 추가
        re = open("student.txt", 'a', encoding='UTF-8')  # txt 문장 추가
        aa = len(student) + 1 # 고유 번호 지정
        bb = 'S' + str(aa) # 고유 번호 생성
        cc = '\n'+ bb + ',' + number +','+ content # 한 문장으로 합치기 number = 이름 content = 전화번호
        re.write(cc) # 글 쓰기



