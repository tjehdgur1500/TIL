# 자바스크립트의 호이스팅

호이스팅은 내가 어렴풋이 알고만 있었지 제대로 알아본적은 없던것 같다.<br><br>

> 호이스팅을 다루게 된 이유는 요즘 부트캠프에 들어오면서 2일차가 인데 <br>
> 페어프로그래밍으로 알고리즘 문제를 풀다 함수관련된 부분을 보고있다가 <br>
> 동료분이 호이스팅에 관해 말씀해주셨는데 그때 " 내가 호이스팅이 뭐였지 ? " 하는 <br>
> 창피한 모습을 보여서 다시한번 명확히 하려고 정리를 한다.

호이스팅(hoisting) 이란 끌어올린다는 표현이다. <br>
우선 호이스팅에 의해 실행의 우선순위가 달라진다고 한다.<br><br>

이런 코드가 있다고 가정한다.

```js
console.log(food)
let food = 'rice'
```

이코드의 결과는 

> Uncaught ReferenceError: food is not defined

이렇게 변수를 찾지 못한다는 에러를 보여준다. 왜그런지 알기전 다른 변수 var 로 동일한 코드를 실행시켜보자


```js
console.log(food)
var food = 'rice'
```

> result : undefined

결과는 undefined 가 나온다.<br>
또 다른 조건을 살펴보자

```js
var food = 'rice'

if (true){
    console.log(food);
    let food = 'rice';
}
```
> result : Uncaught ReferenceError: Cannot access 'food' before initialization

food 라는 변수는 초기화 후에 사용할 수 있다고 한다. <br>
이것은 변수의 선언 단계때문에 그렇다 .


### 변수 선언단계
- 1. 선언단계 : 변수객체에 변수를 등록한다.
- 2. 초기화 단계 : 변수객체에 등록된 변수에 메모리를 할당하고 초기화 시 변수는 undefined 가 된다.
- 3. 할당 단계 : undefined 인 변수에 값을 할당한다.

이제 각 변수마다 어떻게 변수 선언단계가 흘러가는지 알아볼 수 있다.


```js
console.log(food)
let food = 'rice'
```

우선 이 let 은 선언단계에서 food 라는 변수가 생겨났다. <br>
하지만 초기화 단계에서는 실제 let이 사용된 곳에 도착해야하기 때문에 <br>
let 이전에 console.log 가 나와 해당 변수를 찾을 수 없게 된것이다. 
실제 실행시 코드는 이렇다고 보면 되겠다.<br>

```js
let food;
console.log(food) // let을 찾아 초기화를 하기도 전에 food 를 발견해 not defined
let food = 'rice'
```

두번째 var는 위와 동일하나 다른 작동방식을 띈다.<br>

```js
console.log(food)
var food = 'rice'
```

var 는 선언과 초기화를 동시에 한다.<br>
그러므로 초기화 까지 완료가 되었기 때문에 undefined로 나오게 되는것이다.<br>
코드는 이렇다.

```js
var food;
console.log(food) // undefined
var food = 'rice'
```

### const

const 같은 경우엔 선언 후 값을 무조건 할당 하지 않으면 아래와 같은 에러를 볼 수 있다.<br>
 
```js
const food ; // Uncaught SyntaxError: Missing initializer in const declaration
```

### 변수 scope

- var : 함수 범위 스코프 
- let , const 블록 범위 스코프

```js
// 함수 범위 스코프로 동작하는 var

var sum = 1;

{
    var sum = 5;
    console.log(sum) // 5
}

console.log(sum) // 5

```

```js
// 블록 범위 스코프로 동작하는 let
let sum2 = 1;
{
    let sum2 = 5;
    console.log(sum2) // 5
}

console.log(sum2) // 1
```

## Reference

(https://junwoo45.github.io/2020-03-26-hoisting/) <br>
(https://medium.com/sjk5766/var-let-const-%ED%8A%B9%EC%A7%95-%EB%B0%8F-scope-335a078cec04)
