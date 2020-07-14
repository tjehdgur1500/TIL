# 자바스크립트 알고리즘

## 단순 별찍기

### 별을 찍어 삼각형 만들기

Q. 별을 찍어 삼각형 만들기

A. 별문자를 변수에 넣고 반복을 돌때마다 해당 변수에 문자를 붙여주면 된다.

```javascript
function starRepeat(height) {
  var star = "*";
  for (var i = 0; i <= height; i++) {
    console.log(star);
    star += "*";
  }

  starRepeat(5);
  starRepeat(3);
  starRepeat(1);
}
```
