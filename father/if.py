
# 5. 예제 - 로그인 시스템 만들기
아이디 = input("아이디를 입력하세요: ")
비밀번호 = input("비밀번호를 입력하세요: ")

if 아이디 == "admin" and 비밀번호 == "1234":
    print("로그인 성공!")
else:
    print("로그인 실패. 아이디 또는 비밀번호를 확인하세요.")

# 6. 예제 - 가위바위보 게임
player = input("가위, 바위, 보 중 하나를 선택하세요: ")
computer = "가위"  # 컴퓨터는 가위 선택

if player == computer:
    print("비겼습니다!")
elif (player == "가위" and computer == "보") or (player == "바위" and computer == "가위") or (player == "보" and computer == "바위"):
    print("이겼습니다!")
else:
    print("졌습니다!")

# 7. 예제 - 짝수 홀수 판별하기
숫자 = int(input("숫자를 입력하세요: "))

if 숫자 % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")


# 8. 예제 - 7의 배수 만들기
숫자 = int(input("숫자를 입력하세요: "))

if 숫자 % 7 == 0:
    print("7의 배수입니다.")
else:
    print("7의 배수가 아닙니다.")
