# TIL 2021-03-16

## 오늘 배운 내용

---

  - 일급 객체
  - 고차함수
## 일급객체 ( first-class citizen )


일급객체는 자바스크립트에서 특별대우를 받는 객체를 말하는데 <br>
그중 함수가 일급객체에 해당된다. <br><br>

일급객체인 함수는 고차함수라고 부르는데 다음과 같은 특징이 있다.<br><br>

### 특별한 대우를 받는 function 의 경우 특징

- 변수에 할당(assignment)할 수 있다.
- 다른 함수의 인자(argument)로 전달될 수 있다.
- 다른 함수의 결과로서 리턴될 수 있다.

<br>

## 함수 표현식의 경우로 일급객체 보기

함수 선언식과 달리 호이스팅이 일어나지 않는다.

```jsx
// 아래는 변수 square에 함수를 할당하는 함수 표현식이다.
// 자바스크립트에서 함수는 일급 객체이기 때문에 변수에 저장할 수 있다.

// 함수 표현식은 할당 전에 사용할 수 없다.
// square(7); // --> ReferenceError: Can't find variable: square

const square = function (num) {
  return num * num;
};

// square에는 함수가 저장되어 있으므로 (일급 객체), 함수 호출 연산자 '()'를 사용할 수 있다.
output = square(7);
console.log(output); // --> 49
```

이처럼 함수를 변수에 담아서 사용하면 리턴 하는 값을 다른 함수의

인자값으로 사용가능하다.<br><br>
# 고차함수

함수의 인자값으로 함수를 받거나 함수를 리턴하는 함수를 말한다.

이 경우 callback function 을 예로들 수 있다.

```jsx
ele.addEventListner('click', function(){
	console.log('clicked')
})
```

이런 이벤트 메서드에서 두번째 인자로 함수가 있는데 ,

이경우도 callback , 즉 고차함수다.

## 다른 함수를 인자로 받는 경우

```jsx

function double(num) {
  return num * 2;
}

function doubleNum(func, num) {
  return func(num);
}

// 함수 doubleNum은 다른 함수를 인자로 받는 고차 함수
// 함수 doubleNum의 첫 번째 인자 func에 함수가 들어올 경우
// 함수 func는 함수 doubleNum의 콜백 함수
// 아래와 같은 경우, 함수 double은 함수 doubleNum의 콜백 함수
let output = doubleNum(double, 4);
console.log(output); // -> 8
```

콜백 함수를 전달받은 함수는 이 콜백 함수를 호출(invoke)할 수 있다.

caller(함수를 인자로받는 함수)는 조건에 따라 

콜백 함수의 실행 여부를 결정할 수도 있고, 심지어 여러 번 실행할 수도 있다.

특히 콜백 함수는 어떤 작업이 완료되었을 때 호출되는 경우가 많아서 

답신 전화를 뜻하는 콜백이라는 이름이 붙여졌다.

## 함수를 리턴하는 경우

```jsx
function adder(added) {
  return function (num) {
    return num + added;
  };
}

// 함수 adder는 다른 함수를 리턴하는 고차 함수
// adder는 인자 한 개를 입력받아서 함수(익명 함수)를 리턴
// 리턴되는 익명 함수는 인자 한 개를 받아서 added와 더한 값을 리턴

// adder(5)는 함수이므로 함수 호출 연산자 '()'를 사용할 수 있다.
let output = adder(5)(3); // -> 8
console.log(output); // -> 8

// adder가 리턴하는 함수를 변수에 저장할 수 있다.
// javascript에서 함수는 일급 객체이기 때문
const add3 = adder(3);
output = add3(2);
console.log(output); // -> 5
```

## 함수를 인자로 받고, 함수를 리턴하는 경우

```jsx
function double(num) {
  return num * 2;
}

function doubleAdder(added, func) {
  const doubled = func(added);
  return function (num) {
    return num + doubled;
  };
}

// 함수 doubleAdder는 고차 함수다.
// 함수 doubleAdder의 인자 func는 함수 doubleAdder의 콜백 함수다.
// 함수 double은 함수 doubleAdder의 콜백으로 전달되었다.

// doubleAdder(5, double)는 함수이므로 함수 호출 기호 '()'를 사용할 수 있다.
doubleAdder(5, double)(3); // -> 13

// doubleAdder가 리턴하는 함수를 변수에 저장할 수 있다. (일급 객체)
const addTwice3 = doubleAdder(3, double);
addTwice3(2); // --> 8
```