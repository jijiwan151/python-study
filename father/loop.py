# 과일들 = ["사과", "바나나", "포도"]
#
# for 과일 in 과일들:
#     print(과일)
#
# for i in range(0, len(과일들)):  # 1부터 5까지 반복 (6은 포함X)
#     print(i, ' : ', 과일들[i])
#
#
# 단 = int(input("몇 단을 출력할까요? "))
#
# for i in range(1, 10):  # 1~9까지 반복
#     print(f"{단} x {i} = {단 * i}")


비밀번호 = "1234"

while True:  # 무한 루프
    입력값 = input("비밀번호를 입력하세요: ")

    if 입력값 == 비밀번호:
        print("비밀번호가 맞습니다!")
        break  # 정답이면 반복 종료
    else:
        print("틀렸습니다. 다시 입력하세요.")
