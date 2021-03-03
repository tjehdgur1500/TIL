# TIL 2021-03-03

## 오늘 배운 내용

---

- 자바스크립트의 조건문 과 각종 연산자에 대해 알아보았다.

- 문자열에 대해 알아보았다.



## 조건문

> 어느 프로그래밍 언어에나 존재하는 조건문이 자바스크립트에선 어떻게 표현 되는지 살펴보았다. <br>
> if , else if , else 로 조건을 줄 수 있다.<br>
> 다양한 연산자를 알아보았다. <br>
> 아래 예시로 조건문을 살펴본다.<br>

우리가 이런상황에 처한다면 어떻게 행동할까 ? <br><br>

슈퍼에서 3000원 하는 과자를 사려하는데 현재 가진돈이 2500원 밖에 없어 다른과자를 사야한다.<br>
추상적으로는 3000원보다 더 저렴한 과자를 사면 끝난다.<br><br>

그렇다면 이런상황을 코드로 옮긴다면 어떻게 처리해야할까 <br>
여기서 조건문을 살펴볼 수 있다.

```js

function selectSnack(money, snack){

    // 내가 가진 돈과 구매하려는 과자의 가격을 비교한다.
    // 과자의 가격이 내가 가진돈이랑 같거나 가진돈이 더 많다면 구매한다.
    // 과자 가격이 가진돈보다 비싸면 가게를 나간다.

    if (money > snack){
        return `${snack}원의 과자를 구매하였습니다.`
    }else if(money === snack){
        return `${snack}원의 과자를 구매하였습니다.`
    }
    else{
        return `과자가 비싸 가게를 떠났습니다.`
    }
}

selectSnack(3000, 2500)


```
이처럼 프로그래밍은 추상적인 행동을 전부 절차대로 처리해줘야한다. <br>
아니면 중간에 과정이 생략되거나 오류가 나타날것이다. <br>
이렇게 과정을 처리할 수도 있으나 우리는 조금도 효율적인 방법을 찾을 수 있다면 그렇게 하는것이 좋다.<br>
위 코드를 아래와 같이 바꾸어보았다.

```js

function selectSnack(money, snack){

    if (money >= snack){
        return `${snack}원의 과자를 구매하였습니다.`
    }else{
        return `과자가 비싸 가게를 떠났습니다.`
    }
}

selectSnack(3000, 2500)


```
두 함수식의 return 값은 동일하다. <br>
첫번째 함수식은 else if의 쓰임새를 설명하기 위해 일부러 넣었다. <br>
조건문은 이렇게 나눠볼 수 있겠다.

- 만약 .. 이라면 (if)
- ..가 아니고 ..라면 (else if)
- 아니라면 (else)

더 나아가 switch 문도 있지만 주제와 맞지 않으니 다음에 기록해보려한다.

## 문자열

> 자바스크립트에서 문자열을 표현해본다.<br>
> 문자열과 문자열끼리 결합이 가능하고 숫자와도 결합이 가능하다.<br>
> 문자, 숫자를 형변환 할 수 있다.<br>

자바스크립트에서 문자열을 표현할때는 <br>
각각 따옴표로 표현할 수 있다. <br>

single quote (' ') , single quote (" ") , backtick 으로 나뉜다 . 

```js

let firstWord = 'hello', 
    secondWord = "javascript"

```

보이는것과 같이 싱글 , 더블 쿼터로 문자열을 표현했다 . <br>
이제 문자열들을 결합해보자.

```js

let resultWord = firstWord + secondWord

// result 
'hellojavascript'
```
잘 조합 된것처럼 보이지만 뭔가 이상한점이 있다. 띄어쓰기가 안되어서 구별을 할 수가 없다.<br>
자바스크립트에서는 공백도 문자열로 표현한다. 이는 빈문자열과는 다르다.<br>
이것을 이용해서 문자열을 띄울 수도 있다.

```js

let resultWord = firstWord + ' ' + secondWord

// result 
'hello javascript'
```

이제 원하는대로 나왔다. <br>
또 하나 문자열을 표현하는 backtick이다.<br>
backtick 을 이용한 표현방법을 template literal 이라고 표현하는데 이는<br>
ES6 도입후 생겨난 아주 훌륭한 표현방법이라고 생각한다.<br><br>

만일 문자열과 변수를 조합해야한다면 어떻게 할 수 있을지 확인해보자 

```js

// 통상적으로  변수와 문자열을 조합하는 방법

let jsVersion = 'ES8';  

console.log(jsVersion + ' ' + '공부해보자');

//result

"ES8 공부해보자"

```
아주 잘 나올것이다. <br>
하지만 결합해야하는 조건이 매우길거나 복잡하면 일일히 + 와 quote 를 신경쓰며 결합해야한다. <br>
그래서 유용한 backtick 이 있다.


```js

let jsVersion = 'ES8';  

console.log(`${jsVersion} 공부해보자`);

//result

"ES8 공부해보자"

```

결과는 같지만 결합하는 과정에서 달라진다.<br>
template literal 은 ${ } 이렇게 붙여서 사용한다.<br>
괄호안에는 변수가 들어가 자동으로 문자열로 치환해줄것이다. <br>
굉장히 유용하므로 알아두면 좋다.
