import os

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
        fileData.close()
        return

    #강의 정보 모두 받아오기
    ### 아... 이부분 ... open 왜 오류나지...? 이거만 고치면 될듯
    fileData = open('class.txt', 'r', encoding='UTF-8')
    classData = []
    while True:
        line=fileData.readline()
        if not line: break
        line=line.split(',')
        classData.append(line)
    del classData[0]
    myClassList = []
    if isTeacher:
        #자신의 개설강의 저장
        for classDataLine in classData:
            if classDataLine[1]==myID:
                myClassList.append(classDataLine[0])
    else:
        #자신의 수강강의 저장
        studentData = open('student.txt','r', encoding='UTF-8')
        find=False
        while True:
            line=studentData.readline()
            if not line:
                break
            line=line.split(',')
            if line[0]==myID:
                #수강강의 저장
                for i in range(len(line)-3):
                    myClassList.append(line[3+i])
                    find=True
                    break
        if find==False:
            #사용자의 data가 studentData에 없는 경우
            print('error : user ID is invalid')
            fileData.close()
            studentData.close()
            return
        studentData.close()
    print(myClassList)

    #모든 강의정보 출력 ( 자신의 수강 or 개설강의 별표로 표시)
    while True:
        os.system('cls')
        print('========================================')
        for classDataLine in classData:
            print('('+classDataLine[0]+')') #아 강의 이름정보 없네 업데이트까지 대기해야할듯... ㅎ
            print('강사 : '+classDataLine[1])
            print('연락처 : '+classDataLine[5])
            print('강의실 : '+classDataLine[2])
            print('수업 시간 : ') #아.. 수업시간정보도.. 어찌하나..
            print('수용학생인원 : ' + classDataLine[3]+ '명')
            print('========================================')
        print('1. 수강생 정보 확인')
        print('2. 뒤로가기')
        select = int(input('선택 : '))
        if select==1:
            # 1번 시 학생이면 막고 등등..
            if isTeacher:
                print('수강생 정보확인 하는 flow로 이동합니다.')
            else:
                print('이봐.. 학생은 이곳에 들어올 수 없다구..!!!')
        elif select==2:
            # 2번 시 return 시키기
            print('뒤로가기입니다.')
            fileData.close()
            return
        else:
            print('잘못된 입력입니다. 다시 입력해주세요.')
start('T1')
