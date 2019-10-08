import main
import login
import time
import os

t = open("teacher.txt", 'r',encoding='UTF-8')
s = open("student.txt", 'r',encoding='UTF-8')
tdata = t.read()
sdata = s.read()

def start():
    while True:
        print("="*50)
        print(" "*22, "LISEO")
        print("="*50)  # 로그인 화면의 화면 제목

        name = input("사용자의 고유번호를 입력해주세요: ")
        if name in tdata:
            os.system('cls')
            break

        elif name in sdata:
            os.system('cls')
            break

        else:
            print("해당하는 고유번호가 없습니다. 다시 입력해 주세요.")
            time.sleep(2)
            # 화면 지우기 추가할 것=>파이참에는 없는 기능?
            os.system('cls')
            print(login.start()) #2번 반복하여 불러올 시 에러 생김

    print(main.screen())
    t.close()
    s.close()
start()
# name과 불러온 정보 일치시 화면 지운 후 메인 화면 출력 if name == rnumber.
# 고유번호 존재하지 않을 시 오류메시지 출력 후 2초 뒤 모든 화면 삭제 및 로그인 화면 출력

