import main
import time
import os

teacher = open("teacher.txt", 'r',encoding='UTF-8')
student = open("student.txt", 'r',encoding='UTF-8')
while True:
    TeacherData = teacher.readline()
    if not TeacherData:
        break
    TeacherLogin=TeacherData.split(',',maxsplit=3)
    
#StudentData = student.read()

def start():
    while True:
        print("="*50)
        print(" "*22, "LISEO")
        print("="*50)  # 로그인 화면의 화면 제목

        name = input("사용자의 고유번호를 입력해주세요: ")
        if name in TeacherData:
            os.system('cls')
            break

        elif name in StudentData:
            os.system('cls')
            break

        else:
            print("해당하는 고유번호가 없습니다. 다시 입력해 주세요.")
            time.sleep(2)
            # 화면 지우기 추가할 것=>파이참에는 없는 기능?
            os.system('cls')
        # 반복문 안에 있으므로 start()를 굳이 다시 쓸 필요 없다.

    teacher.close()
    student.close()
# name과 불러온 정보 일치시 화면 지운 후 메인 화면 출력 if name == rnumber.
# 고유번호 존재하지 않을 시 오류메시지 출력 후 2초 뒤 모든 화면 삭제 및 로그인 화면 출력

