import time

print("="*50)
print(" "*18,'1. 마이페이지')
print(" "*18,'2. 강의 정보 열람')
print(" "*18,'3. 내 강의')
print(" "*18,'4. 학생 관리')
print(" "*18,'5. 종료')
print("="*50)

select=input("원하시는 항목을 선택해 주세요.")
if select==1: #마이페이지
elif select==2: #강의 정보 열람
elif select==3: #내 강의
elif select==4: #학생 관리
elif select==5: #종료
    exit()
else:
    print("1-5사이의 항목을 선택해 주세요.")
    time.sleep(2)
    #모든 화면 지우기
    #메인화면 출력