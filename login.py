import time

print("="*50)
print(" "*22, "LISEO")
print("="*50)  # 로그인 화면의 화면 제목

t=open("teacher.txt",'r')
s=open("student.txt",'r')
tdata = t.read()
sdata = s.read()

name = input("사용자의 고유번호를 입력해주세요: ")
if name in tdata:
    print('정답')
    #로그인화면 출력해야함
elif name in sdata:
    print('정답')
    #로그인화면 출력해야함
else:
    time.sleep(2)
    # 화면 지우기 추가할 것=>파이참에는 없는 기능?
    print('오답')

t.close()
s.close()

# name과 불러온 정보 일치시 화면 지운 후 메인 화면 출력 if name == rnumber.
# 고유번호 존재하지 않을 시 오류메시지 출력 후 2초 뒤 모든 화면 삭제 및 로그인 화면 출력

