def calculate(target_number):
    for i in range(1, 10):  # 1~9까지 반복
        print(f"{target_number} x {i} = {target_number * i}")
    #
    # return 결과  # (필요한 경우)


dan = int(input('구구단 숫자 입력 : '))
calculate(dan)
