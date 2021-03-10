# TIL 2021-03-10

## 오늘 배운 내용

---

  - Primitive type , Reference type 의 차이
  - Scope 
  - Closure
  - Rest syntax , Spreed syntax

## Primitive type , Reference type 의 차이

### 원시타입과 참조타입 
<br>

#### 원시타입

  > 원시타입은 stack 이라는 공간에 저장이 된다. <br>
  > stack에 저장되는 값들은 각각의 공간에 위치해 있다. <br>
  > 원시타입에는 하나의 값만 들어갈 수 있다.<br>
  > 원시타입은 비교 시 값 과 값을 비교한다.

내가 정리한 원시타입이다. <br>
살펴보자면 stack 공간 , 각각 개별공간에 위치 , 하나의 값만 존재 가능 , 비교시 값과 값 인데 <br>

코드로 보면 매번 쓰는 이것이다.<br><br>

```js
let stack1 = 'hello', // stack에 위치하고
    stack2 = 'hello'; // stack 변수라는 각각 공간에 하나의 원시타입 값이 위치

let errorStack3 = 'hello', 1  // 하나의 값이 아니라 에러 발생

if (stack1 === stack2) // 스택에 있는 변수의 값과 값을 비교한다.
```
