# TIL 2021-03-22

## replace , replaceAll

자바스크립트에는 원하는 문자열로 치환해주는 
String.prototype.replace 메서드가 존재한다.

```js
let myString = 'hello'
myString.replace('l', 'o');

// heolo
```

단 replace 는 딱 한번만 바꾸기 때문에 여러개의 문자열을 바꾸려면
```js
let myString = 'hello'
myString.replace('l', 'o');
myString.replace('l', 'o');
```
이런식으로 해당 문자가 존재하지 않을때까지 치환하거나 , 정규식을 이용해야할것이다.
그러나 이방법은 너무 불편하다.

내가 문제해결을 위해 replace를 사용하던중
replaceAll이 개발자도구에서 실행이 되는것을 확인했다.

근데 내가 문제푸는 코드스테이츠 코플릿사이트에서는 이를 허용하지 않았다.
무슨 문제때문일까.. 생각하다가 이 replaceAll 기능이 원래 존재 하지 않았다는것과
ECMA에 들어가서 보니 
replaceAll 은 ECMA 2022 에 신규 추가된 메서드였다.

[MDN - replaceAll](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)

mdn에서도 확인가능하다.

```js
let myString = 'hello'
myString.replaceAll('l', 'o');
```

즉 이제 자바스크립트에서도 replaceAll을 사용할 수 있다는 말이다.
실제 시간복잡도가 어떻게 흘러가는지는 조금더 알아봐야겠지만 당장쓰는데에는 문제없지 않을까 ?
야호 !


[ECMAscript - replaceAll](https://tc39.es/ecma262/#sec-string.prototype.replaceall)