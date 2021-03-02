# TIL 2021-03-02

## 오늘 배운 내용

---

- 자바스크립트 변수와 변수타입에 대해 이해했다.

- 원시타입 , 참조타입을 이해했다.

- 기본적인 함수개념에 대해 이해했다.<br>


## 변수

> 변수와 타입 <br>
> 자바스크립트에는 값(데이터)을 담을 수 있는 변수가 존재한다.<br>
> 이 변수들은 각각 이름을 가지고 특정 값들을 보관할 수 있다.<br>
> 아래 예시는 변수에 값을 담고 있는 예제이다.<br>


```js

  var testVariable = 'test';
  let testVariable2 = 1234;
  const pi = 3.14159;

```
<br>
구체적인 설명을 덧붙이자면 변수를 쓰려면 우선 선언이란것을 해야한다.<br>
'선언'이란 일종의 초기화라고 볼 수 있다. <br>
선언을 해야만 이 변수들을 인식하고 사용할 수 있는것이다.<br>
위와 같이 let , const Keyword를 이용해 변수를 만들 수 있다.
<br><br>
여기서 특이한 점이 있는데, 변수들은 각각 변수 타입이 존재한다.<br>

### var
<br>
var 키워드는 굉장히 오래된 변수 타입인데 , 요근래엔 사용하지 않는다. 이유는 너무 오래되고 <br>
관대하여 데이터가 의도치않게 바뀌어버리는 불상사가 생길 수 있기 때문이다. 이덕분에 어떠한 에러도 보여주지 않고 <br>
정상적으로 넘어가는것 처럼 보여진다. 그러므로 패스
<br>
### let, const
<br>
let, const는 var와는 다른 변수타입이다. <br>
이 타입들은 var 를 보완하기 위해 ES6에 도입되었는데 , <br>
우선 변수들은 scope(변수의 범위) 에 따라 사용 가능,불가능이 나뉜다.<br>
이 let, const는 그러한 scope도 지키고 var보다 엄격한 타입이다.<br>
물론 let은 선언한 변수에 재할당을 할 수 있으나 독특한점은<br>

#### 
```js
if (true){
    let x = 'yes!';
}

if (true){
    const y = 'no!';
}

console.log(x);
console.log(y);
```
두 log의 result는 모두 이러한 에러가 나올 것이다.

```js
VM199:5 Uncaught ReferenceError: x is not defined
```
## Block Level Scope
이유는 let , const 는 <br> block 문 안에서 선언했으면 이 괄호 밖에선 찾을 수 없기 때문이다. <br>
이것이 블록레벨 범위이며 let , const의 특징중 하나다. 다른 특징으로는 이렇다.<br>

- let : 선언된 변수에 값을 재할당 할 수 있다.
- const : 선언된 변수에 어떠한 값도 재할당 할 수 없는 상수이다.


## 원시타입 , 참조타입

> 자바스크립트 자료타입은 <br>
> 원시타입과 참조타입이 존재한다.<br>

- 원시타입 : String , Number , boolean, undefined
- 참조타입 : Array , Object

### 원시타입 

원시타입은 기본형이라고 볼 수 있는데 순서대로 

```js
// String
typeof '나는 문자열'

// Number
typeof 1996

// boolean
typeof true

// undefined
typeof undefined

```

이 네가지 원시타입을 console.log로 찍어보면 결과는 차례대로<br>
'string' , 'number' , 'boolean', 'undefined' <br>
이렇게 나올 것이다. 각자가 가진 타입이다.<br>

```js
let num = 1;
let num2 = num+2;
``` 
이렇게 사용했을때 둘의 결과는 1 , 3 이 나올것이다.<br>
변수를 다른 변수에 할당해도 영향을 주지 않는다. <br>

참조타입은 조금 다르다.
```js
let array1 = [];
let status = {
    name : 'Seo',
    age : 26
}
```
이런 형태가 참조타입이며 객체라고도 부른다. <br>
잠시 뒤 기록할 함수도 객체이다.<br>

객체타입은 참조를 하기 때문에 위와 같이 다른 변수에 객체 값을 할당하면 영향을 준다. <br>
```js
let status = {
    name : 'Seo',
    age : 26
}

let status2 = status;

{name: "Seo", age: 26}
```
여기까지는 같은 결과를 보인다.<br>
하지만 처음 status 변수값을 바꾼다면 어떤결과를 보이는지 보겠다.

```js
status.name = 'Kim';

console.log(status.name)
console.log(status2.name)

'Kim'
'Kim'
```
이렇게 나올 것이다. <br>
이 타입은 참조 타입임을 기억해야한다. <br>
처음 객체의 값이 바뀌면 그 객체를 참조하고 있던 다른 것도 같이 바뀐다.

## 함수 

> 함수는 어떤 기능을 하는 코드모음을 작동하게 하는 요소다.<br>
> 사실 함수는 깊게 들어가면 정말 복잡해지지만 여기선 간단하게 다뤄보려한다.<br>


함수는 선언 , 호출 이 있다.
```js
// 함수 선언
function myFunction(a, b){
    return a * b
}

//  또는

let myfunction = function(a, b){
    return a * b
}

myfunction(5, 10);
```

보통은 이렇게 쓰곤한다. <br>
근데 여기서 괄호안 숫자 두개가 있고 함수 선언부에는 a , b 라고 있다. <br>

함수 선언부분에서는 매개변수 (parameter) <br>
함수 호출부분에서는 인자 (argument) 라고 부른다. <br>

### parameter
- 매개변수는 함수 내부에서 사용하기 위한 일종의 변수다.
- 이름은 자유롭게 해도 되나 함수 의도대로 짓는게 옳다고 본다.

### argument
- 인자는 함수 호출부분에서 전달할 값을 말한다.
- 호출부분에서 선언부분으로 전달한다.

함수 호출은 선언부분으로 돌아가서 순서대로 실행되게끔 되어있어 , <br>
매개변수로 들어온 인자값을 이용해 함수를 만들어 나갈 수 있다.
