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