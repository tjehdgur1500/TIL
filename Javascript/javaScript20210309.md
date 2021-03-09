# TIL 2021-03-09

## 오늘 배운 내용

---

  - 배열의 사용법을 알았다.

## 배열

### Array

> 배열도 객체의 일부이다. <br>
> 배열은 iterable 한 객체이고 순서가 보장된다.

배열은 기본적으로 여러 타입의 데이터를 담을 수 있다.
사용방법은 아래와 같이 쓰면 된다.

```js

// 기본적인 배열 init
let myArr = [];
let myArr2 = [1,'2',myVar, myFunc, [1,2,3]]

```
위 처럼 배열안 중첩배열을 넣을 수 도 있고 함수도 넣을 수 있다.<br><br>

배열을 처음 초기화 시키면 undefined 상태이다.<br>

배열에 값을 추가하거나 제거 하고 싶을때 유용한 메서드들이 있다.

- push ( 배열의 끝에 데이터를 추가한다. )
- pop ( 배열의 끝에 있는 데이터를 제거한다. )
- unshift ( 배열의 앞에 데이터를 추가한다. )
- shift ( 배열의 앞에 있는 데이터를 제거한다. )
  

```js

myArr.push('Hello') // ['hello']
myArr.pop() // []
myArr.unshift('javascript',2) // ['javascript', 2]
myArr.shift() // [2]

```
이렇게 데이터를 추가 제거 할 수 있으며 수정도 가능하다.

```js
let myArr = ['hello', 'javascript'] ;

myArr[1] = 'typescript'

```
보는바와 같이 변수명 앞에 있는 [] 브라켓안에 있는 숫자는 index를 뜻한다.  <br>
배열에서 index 란 배열의 순서를 말하며 여기서 배열은 순서가 보장된다는것을 알 수 있다. <br><br>

index 는 0 번째 부터 시작한다. <br>
이런 순서특성을 이용해 for 문을 사용할 수 있다.

```js

let myArr = ['hello', 'javascript'] ;

for (let i=0; i < myArr.length; i++){
    myArr[i]
    // 'hello'
    // 'javascript'
}

```
또한 이런 기본적인 반복문이 아닌 객체나 , 순회가능한 객체를 위한 반복문도 존재한다. <br>

- for...of
    > for...of 명령문은 반복가능한 객체 (Array, Map, Set, String, TypedArray, arguments 객체 등을 포함)에 대해서 반복하고 각 개별 속성값에 대해 실행되는 문이 있는 사용자 정의 반복 후크를 호출하는 루프를 생성합니다.<br>  - MDN for...of 참조 -

<br>
쉽게 말하면 반복가능한 모든 요소들은 for of 를 사용할 수 있다.<br>
코드로 보면<br>

```js
let myArr = ['1', '2', '3', 4, 5, 'hi']
for (ele of myArr){
    console.log(ele)
}
// '1'
// '2'
// '3'
//  4
//  5
// 'hi'
```
기존 반복문 보다 더 간략하게 되었지만 길이를 비교해야하는 무언가를 수행하려면 <br>
기존 반복문을 써야할것이다. <br>
상황에 맞게 쓰면 될것 같다. <br><br>
