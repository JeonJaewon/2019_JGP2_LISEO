def numberRule(number): #1.1에서 2^31-1의 정수 2.띄어쓰기 불가 3.최고 자릿수 0 불가 4.아스키코드 불가
    for i in range(len(number)):
        if number[i]<'0' or number[i]>'9': #규칙2 띄어쓰기 와 규칙4 아스키코드
            print("숫자입력규칙에 어긋납니다.") #실험용
            return 0
    if number[0] == '0': #규칙 3 최고 자릿수 0
        print("숫자입력규칙에 어긋납니다.") #실험용
        return 0
    if len(number)>10:
        print("숫자입력규칙에 어긋납니다.") #실험용
        return 0
    return 1  # 성공하면 1을 출력, 실패하면 0을 출력!