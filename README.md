# python-study

## git 명령어
### 복제 할 때 (git clone)
```shell
git clone https://github.com/jijiwan1151/~~~~
```

### 수정 된 내용을 커밋할 때 (git add / git commit)
```shell
git add .
git commit -m '무슨 내용을 수정 했는지'
```

### push 할 때 (git push)
```shell
git push
```

### pull 할 때 (git push)
```shell
git pull
```


# exe 만들기 위해서 가상 환경 만들기

##  가상환경(env)사용하기 권장
```shell
# 가상 환경 만들기
python3 -m venv myenv

# 가상 환경 활성화
source myenv/bin/activate

# 이제 pip 설치 가능!
pip install 원하는패키지
```

## 현재 가상환경인지 확인하기
```shell
which python3  # 윈도우일 경우 python
```

## 가상 환경 나가기
```shell
deactivate
```


# tkinter 강좌
https://076923.github.io/posts/Python-tkinter-2/