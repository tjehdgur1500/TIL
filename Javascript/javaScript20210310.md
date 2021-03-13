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

  ##  원시타입

  > 원시타입은 stack 이라는 공간에 저장이 된다. <br>
  > stack에 저장되는 값들은 각각의 공간에 위치해 있다. <br>
  > 원시타입에는 하나의 값만 들어갈 수 있다.<br>
  > 원시타입은 비교 시 값 과 값을 비교한다.
<br><br>

내가 정리한 원시타입이다. <br>
살펴보자면 stack 공간 , 각각 개별공간에 위치 , 하나의 값만 존재 가능 , 비교시 값과 값 인데 <br>

코드로 보면 정말 간단하면서 원래 알고 있었던 것들이다.<br>

```js
let stack1 = 'hello', // stack에 위치하고
    stack2 = 'hello'; // stack 변수라는 각각 공간에 하나의 원시타입 값이 위치

let errorStack3 = 'hello', 1  // 하나의 값이 아니라 에러 발생

if (stack1 === stack2) // 스택에 있는 변수의 값과 값을 비교한다.
```

하지만 해당 원시타입들이 어떻게 어디에 저장되는지 더 깊게 볼 수 있겠다. <br>
변수에 저장하는건 맞지만 stack 이라는 공간에 각각 변수가 위치하는것이다.


## 참조타입

  > 참조타입은 heap 이라는 공간에 저장한다. <br>
  > heap 각각 임의의 주소와 주소값을 가진다. <br>
  > 주소와 주소값을 가진 참조형 값은 stack에 저장한다. <br>
  > 동일해보이는 참조타입 끼리 비교해보면 서로 동일 하지 않은 결과를 나타낸다.
<br><br>

참조타입은 이렇게 볼 수 있다.

```js

if ([] === [])

```

해당 결과값은 어떻게 나올까 ? <br>
바로 false 나온다. <br><br>

위에도 말했듯 참조타입은 heap 에 각자 주소와 주소값을 가지고 있다.<br>
그렇다면 저 두 배열은 서로 다른 주소값을 바라보고 있기 때문에 <br>
비교시 stack에 있는 값이 아닌 주소값을 비교하는 것으로 볼 수 있다.

```js
let obj = {
  a : 1,
  b : 2
}

let refObj = obj;
refObj.a = '1000'
```

위 obj 의 a 값은 어떻게 나올까 <br><br>

```js

refObj.a // '1000'
obj.a // '1000'

```

이렇게 원본 값이 바뀌어버린다. <br>
이또한 서로 바라보는 주소값이 같아서인데 , <br>
refObj 는 obj를 할당했을때 obj의 주소값을 바라보게 되기 때문에 <br>
둘중 하나의 값이 바뀌면 둘다 동일하게 바뀌게 되는것이다.


## Scope

### block level Scope , function level Scope

이번엔 변수의 범위에 대해 말해보려 한다. <br><br>

## global && local 변수

코드로 한번 설명해보자면 변수는 전역변수 와 지역변수로 나뉜다.<br>

```js

let variable1 = 'hello'

function test(){
  variable1 = 'hi'
  return variable1
}

test(); // hi
console.log(variable1) // hi

```

각자의 값은 함수 내부에서 변수에 값을 재할당 함으로써 <br>
재할당한 값으로 바뀌어버렸다. <br><Br>

이런 경우에 전역변수라고 부를 수 있겠다. <br>
즉 어디에서나 접근 가능한 범위이다. <br><br>

이제 지역변수를 살펴보자

```js

let variable1 = 'hello'

function test(){
  let variable1 = 'hi'
  return variable1
}

test(); // hi
console.log(variable1) // hello

```

지금은 아까와 다르게 함수안에서 let 키워드로 변수를 선언했다. <br>
우선 함수가 실행되었을때 block ( 자신의 범위 ) 안에서 변수를 먼저 찾는다. <br><Br>

자신의 범위안에 변수가 할당이 아닌 선언이 되었기 때문에 함수는 이 지역 변수를 리턴하므로 <br>
전역변수와는 전혀 상관없는 값을 리턴하는 것이다.<br><Br>

이런경우를 Block level Scope  라 부른다. <br><br>
전역변수를 사용하는 경우 Function level Scope 라 부른다. <br><br>


```js

let variable1 = 'hello'

function test(){
 let variable1 = 'hi'

  function test2(){
    return variable1 = 'nice';
  }
  return test2()
}

test(); // nice
console.log(variable1) // hello

```

이 경우에도 마찬가지로 지역범위 내에서 먼저 찾는다. <br><Br>

내 생각엔 전역변수를 너무 남발하지 않도록 조심해야할것 같다. <br>
너무 많은 변수로 인해 언제 어디서 이 변수를 사용할지 모르기때문이다. 

## Closure

### 클로저

클로저는 함수 안의 내부함수를 리턴하는 경우를 말하는데  , <br>
내부함수가 정의되고 나서 만들어진 환경 (클로저) 을 기억한다. <br>
그래서 외부함수의 변수를 사용할 수 있다. <br><br>

클로저를 이용하면 private 한 정보도 은닉화 시킬 수 도 있고 , <br>
모듈패턴도 만들 수 있지 않을까 싶다.

```js

let outerFunc = function(arg1){
    return function(arg2){
        return `${arg1} 을 저장 , ${arg2} 도 사용한다.`
    }
}

let innerCall = outerFunc('첫번째 값');
innerCall('두번째 값')

// "첫번째 값 을 저장 , 두번째 값 도 사용한다."

```
클로저는 이런식으로 사용할 수 있다. <br>
장점은 역시 은닉화 , 재사용성에 용이하다. <br>
그렇다면 단점은 없을까 ?? 

- 클로저의 단점
  > <br>일반 함수였다면 함수 실행 종료 후 가비지 컬렉션(참고 자료: MDN '자바스크립트의 메모리 관리') 대상이 되었을 객체가, 클로저 패턴에서는 메모리 상에 남아 있게 된다. 외부 함수 스코프가 내부함수에 의해 언제든지 참조될 수 있기 때문이다. 따라서 클로저를 남발할 경우 퍼포먼스 저하가 발생할 수도 있다.
  <br><br>

무분별한 클로저 사용은 좋지 않다고 말하는것 같다.<Br>
클로저의경우 메모리 상에 남아있게 된다는걸 기억해야겠다.

##  Rest syntax , Spreed syntax

### Rest syntax 

만약 수많은 인자값을 가지고 하나로 합치려면 

```js

let test = function(arg1,arg2,arg3,arg4,arg5,arg6){
  console.log(arg1,arg2......)
}


test(1,2,3,4,5,6)

```

굉장히 번거운 작업을 해야할 수 있다. <br>
나는 보기에도 좋지 않다고 생각한다. <br>
이럴때 Rest syntax 를 사용하면 이 많은 매개변수를 안써도 된다. 

```js

let test = function(x,...arg){
  console.log(x)
  console.log(arg)
}


test(1,2,3,4,5,6)

// 1
// [2,3,4,5,6]
```

... 세개를 붙이는것만으로도 배열을 만들어서 반환한다. <br>
Rest syntax 는 무조건 배열을 반환하게 되어있어 값이 얼마나 들어오든 <br>
배열객체로 만들어준다. <br><br>

이것과 비슷한 arguments 객체가 있는데 , <br>
arguments 는 전달된 모든인자를 가지고 유사 배열로 만든다 . <br><br>

Rest syntax 는 함수 표현에 지정되지 않은 모든것 (...arg 에 포함된) 만 배열로 만든다.<br>
이렇게 만들어진 배열은 실제 배열이 되므로 관련 메서드를 사용가능하다.<br><br>

반면에 arguments 객체는 길이확인을 위한 length를 제외한 배열관련 메서드를 사용할 수없다.


### Spreed syntax

Spreed 는 rest 와는 반대로 객체를 펼친다. <br>


```js

let test = function(x, y, z){
  return x + y + z
}

test(...[3,4,5])

// result : 12
```
객체를 펼친다는것은 값들을 원시타입으로 만든다는것으로 위처럼 <br>
각 매개변수로 전달되어 연산이 가능하다. <br><br>
또한 얕은복사도 가능하다.

```js

let arr1 = [1,2,3]
let arr2 = [...arr1]
arr2.push(4);

// arr2 => 1,2,3,4
// arr1 => 1,2,3

```

하지만 깊은 상위객체아래 내부객체가 있는경우를 복사하는 경우는 적합하지 않다고 한다.<br>

```js

let test = function(...arg){
  arg[0].key1 = 'hello'
  return arg
}

let a = {
  key1 : '1',
  key2 : '2'
}

let b = {
  key3 : '3',
  key4 : '4'
}

test(a,b)

// return : [0: {key1: "hello", key2: "2"} 1: {key3: "3", key4: "4"}]

// a : {key1: "hello", key2: "2"}
```
이렇게 내부객체는 복사하는게 아닌 주소를 공유해버리기 때문이다. <br><br>
MDN 에서도 이렇게 이야기 하고 있다. <br><br>

> <br> 참고: Spread 문법은 배열을 복사할 때 1 레벨 깊이에서 효과적으로 동작합니다. 그러므로, 다음 예제와 같이 다차원 배열을 복사하는것에는 적합하지 않을 수 있습니다. (Object.assign() 과 전개 구문이 동일합니다)<br><br>

여러모로 유용한 문법이니 적재적소 잘 활용하면 좋을듯 하다.