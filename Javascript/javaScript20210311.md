# TIL 2021-03-11

## 오늘 배운 내용

---

  - loose equality 와 strict equality 의 차이
  - test case 프레임워크 mocha 

## loose equality 와 strict equality 의 차이

### 느슨한 , 엄격한 일치연산자
<br>

##  두 연산의 차이

  > 타입까지 비교하는지 , 타입변환을 하는지가 비교 포인트다.
<br>

```js

1 == '1' // => true
"" == false // => false

1 === '1' // => false
"" === false // => true
```

### loose equality  

간단히 말해 loose equality 는 <br>
타입을 비교하지 않고 자신일아 맞는 타입으로 바꿔버린다. <br>
이러면 나중에 개발할때 매우 혼란스러워질 수 있는 위험이 있다. <br><br>

난 이전 실무에서 이방법을 고수해 , 나중에 고생했던 경험이 있다. <br>

### strict equality 

strict equality 는 <br>
타입까지 엄격하게 비교하기 때문에 위의 느슨한 비교보다 더 확실하게 비교처리를 할 수 있다. <br>
아무리 생각해도 이방법이 맞다고 생각든다.

## Test Case 프레임워크  mocha 

### mocha

![](https://heropy.blog/css/images/vendor_icons/mocha.png)

자바스크립트는 TDD , BDD 같이 단위별로 테스트할 필요가 처음엔 없었다고 한다. <br>
그런데 개발규모가 커지면서 함수단위로 제대로 된 값을 반환하는지 하는 과정을 테스트할 필요가 있어졌고 , <br>

이중 mocha 는 테스트러너를 지원하는 테스트 프레임워크다. <Br>
TDD , BDD 를 위한 라이브러리 chai , Should.js  도 존재한다. <br>

난 파이썬에서 테스트코드를 작성해본적이 있었는데 , <br>
자바스크립트에도 이런 테스트 프레임워크가 있는줄 몰랐다.<br><Br>

사용 방법은 npm 을 이용해 설치하고

```
npm install mocha -g
```

app.spec.js 파일을 만들어 테스트할 코드를 require 로 가져와서 사용한다고 한다. <br><br>

mocha 는 내가 직접 테스트 단위로 개발할때 직접 써보면서 다시 정리해야겠다.<br>
지금은 이런 유용한 프레임워크도 있구나 정도만 생각해야겠다.
