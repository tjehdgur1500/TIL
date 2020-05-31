# 백준 알고리즘

## 조건문

### 2. 두 수 비교하기

Q. 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

A. 두수를 정수값으로 받은다음 `if elif` 조건으로 확인할 수 있다.

```python

A, B = map(int, input().split())
if A > B :
    print(">")
elif A < B :
    print("<")
elif A == B :
    print("==")

```

### 2. 시험 성적

Q. 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

A. 각 조건에 시험점수 최소범위를 받아 입력 값이 범위안에 해당하거나 더 크면 등급을 출력하게 할 수 있다.

```python

score = int(input())
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

```
