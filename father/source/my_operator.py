a = 10
b = 5

print(a > b)   # True (10이 5보다 크다)
print(a < b)   # False (10이 5보다 작지 않다)
print(a == 10) # True (a는 10과 같다)
print(b != 10) # True (b는 10과 다르다)
print(type(b != 10)) # True (b는 10과 다르다)
print(type(str(b != 10)))

# 3. if 문과 비교 연산자 사용하기
나이 = int(input("당신의 나이는? "))

if 나이 >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 4. 실전 예제 - 숫자 맞추기 게임
정답 = 7
사용자입력 = int(input("숫자를 맞혀보세요! "))

if 사용자입력 > 정답:
    print("너무 커요! 더 작은 숫자를 입력해보세요.")
elif 사용자입력 < 정답:
    print("너무 작아요! 더 큰 숫자를 입력해보세요.")
else:
    print("정답입니다! 🎉")
