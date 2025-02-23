# a = 3
# b = 4
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# if a > b:
#     print("정답")
# else:
#     print("오답")

from decimal import Decimal

age = Decimal(input("나이을 입력하시오 : "))
print(age)
if age >= Decimal("19"):
    print("어서오십시오")
else:
    print("나가세요")