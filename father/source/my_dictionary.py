학생 = {
    "이름": "철수",
    "나이": 12,
    "학교": "서울초등학교"
}

print(학생)
# 출력: {'이름': '철수', '나이': 12, '학교': '서울초등학교'}

# 2. 딕셔너리에서 값 가져오기 (dict[key])
print(학생["이름"])

# 3. 딕셔너리 값 변경하기
# 딕셔너리는 리스트와 다르게 키를 사용해서 값을 변경할 수 있어!
학생["나이"] = 13  # 나이를 13으로 변경
print(학생["나이"])  # 출력: 13

# 4. 딕셔너리에 새로운 데이터 추가하기
학생["반"] = 5  # 새 키-값 추가
print(학생)
# 출력: {'이름': '철수', '나이': 12, '학교': '서울초등학교', '반': 5}

# 5. 딕셔너리에서 데이터 삭제하기 (del)
del 학생["학교"]  # "학교" 키 삭제
print(학생)
# 출력: {'이름': '철수', '나이': 12}

# 6. 딕셔너리에서 모든 키와 값 확인하기 (keys(), values(), items())
학생 = {
    "이름": "철수",
    "나이": 12,
    "학교": "서울초등학교"
}

print(학생.keys())   # 출력: dict_keys(['이름', '나이', '학교'])
print(학생.values()) # 출력: dict_values(['철수', 12, '서울초등학교'])
print(학생.items())  # 출력: dict_items([('이름', '철수'), ('나이', 12), ('학교', '서울초등학교')])

# 7. 딕셔너리 반복문 (for)
학생 = {
    "이름": "철수",
    "나이": 12,
    "학교": "서울초등학교"
}

for 키, 값 in 학생.items():
    print(키, ":", 값)

# 8. 실전 예제 - 전화번호부 만들기
전화번호부 = {
    "엄마": "010-1234-5678",
    "아빠": "010-8765-4321",
    "친구": "010-1111-2222"
}

이름 = input("찾을 이름을 입력하세요: ")
if 이름 in 전화번호부:
    print(f"{이름}의 전화번호: {전화번호부[이름]}")
else:
    print("등록되지 않은 이름입니다.")
