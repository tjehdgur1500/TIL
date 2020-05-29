# 백준 알고리즘

## 입출력 사칙연산

### 1. Hello World

Q. Hello World!를 출력하시오.

A. Hello World! 를 `print()`로 출력해주면 된다.

```python

print("Hello World!)

```

### 2. We love kriii

Q. ACM-ICPC 인터넷 예선, Regional, 그리고 World Finals까지 이미 2회씩 진출해버린 kriii는 미련을 버리지 못하고 왠지 모르게 올 해에도 파주 World Finals 준비 캠프에 참여했다.

대회를 뜰 줄 모르는 지박령 kriii를 위해서 격려의 문구를 출력해주자.

A. 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다. `print()` 를 사용하여 문장을 출력한다.
또는 for문을 사용하여 2번 출력하게 만들 수 있다.

```python

print("강한친구 대한육군")
print("강한친구 대한육군")

for _ in range(2) :
    print("강한친구 대한육군")

```

### 3. 고양이

Q. 고양이를 출력한다.

A. `print()`를 이용해 고양이 모양이 나오게 출력한다.
DocType 으로 해도 되지만 라인마다 `print()`를 두어 출력되게 할 수 있다.

```python

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

```

### 4. 개

Q. 개를 출력한다.

A. `print()`를 이용해 개 모양이 나오게 출력한다.
DocType 으로 해도 되지만 라인마다 `print()`를 두어 출력되게 할 수 있다.

```python

print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\ ")
print("|\"^\"`    |")
print("||_/=\\\\__|")

```

### 5. A+B

Q. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

A. `input()`으로 두 정수를 변수에 할당해 더하는 연산을 `print()` 로 출력 해준다.
두수를 한줄씩 받아도 되지만 `map()` 함수를 이용해 입력값을 int 형 으로 캐스팅후 공백을 기준으로 `split()`을 이용해 잘라서
할당할 수도 있다.
```python

A, B = map(int, input().split())
print(A + B)

```

### 6. A-B

Q.두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

A. `input()`으로 두 정수를 변수에 할당해 빼는 연산을 `print()` 로 출력 해준다.
두수를 한줄씩 받아도 되지만 `map()` 함수를 이용해 입력값을 int 형 으로 캐스팅후 공백을 기준으로 `split()`을 이용해 잘라서
할당할 수도 있다.  
또는 `input()` string 형태로 받고 출력시 `int(A) - int(B)` 형태로 해도 같은 결과를 출력한다.
```python

A, B = map(int, input().split())
print(A - B)

```

### 7. A*B

Q.두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

A. `input()`으로 두 정수를 변수에 할당해 곱하는 연산을 `print()` 로 출력 해준다.
두수를 한줄씩 받아도 되지만 `map()` 함수를 이용해 입력값을 int 형 으로 캐스팅후 공백을 기준으로 `split()`을 이용해 잘라서
할당할 수도 있다.
```python

A, B = input().split()
print(int(A) * int(B))

```

### 8. A/B

Q.두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

A. `input()`으로 두 정수를 변수에 할당해 나는 연산을 `print()` 로 출력 해준다.
두수를 한줄씩 받아도 되지만 `map()` 함수를 이용해 입력값을 int 형 으로 캐스팅후 공백을 기준으로 `split()`을 이용해 잘라서
할당할 수도 있다.
```python

A, B = input().split()
print(int(A) / int(B))

```

### 9. 사칙연

Q.두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

A. 두 정수를 받는데 한줄로 받기위해 `map(int, input().split())` map 함수를 이용해 int로 캐스팅하고
`split` 함수로 공백을 기준으로 해서 각각 변수에 언패킹한다.
그리고 각 줄마다 `print()`에 연산을 넣어 출력하게 만들면 된다.  
물론 내가 작성한 코드는 하나하나 int 캐스팅을 하였다.
```python

a, b = input().split()
print(int(a) + int(b))
print(int(a) - int(b))
print(int(a) * int(b))
print(int(int(a) / int(b)))
print(int(a) % int(b))

```

### 10. 나머지

Q. (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오. 

A. 문제에서 요구한것처럼 정수를 받는 변수들을 `if elif` 조건을 걸어서 판별해줄 수 있다. 
```python

A, B, C = map(int, input().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

```

### 11. 곱셈

Q. (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

<img src="img/question11.png" width="306" height="183">

(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오. 

A. 첫번째 정수를 두번째 정수와 곱하는데 두번째 정수의 각 `index`에 접근해서 곱하고
마지막은 전체 값을 출력하게 만든다.
 
```python

a = input()
b = input()
print(int(a) * int(b[2]))
print(int(a) * int(b[1]))
print(int(a) * int(b[0]))
print(int(a)*int(b))

```
