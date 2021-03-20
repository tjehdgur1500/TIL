# TIL 2021-03-21

## Web Storage 사용

간혹 이런경우를 구현하고 싶을때가 있다. 

내가 작성한 리스트를 현재 창에서 벗어나거나 , 새로고침을 했을때도
내가 썼던 리스트가 저장되있는 기능의 경우다.

보통 DB를 이용하면 template 엔진을 통해서 리스트를 뿌려주면 된다.
하지만 DB가 아닌 클라이언트 상에서 저장해야하는 상황이라면 이야기가 달라진다고 볼 수 있다.

우선 내경험으로는 최근 검색어같은 경우도 쿠키 or storage 라고 생각한다.

그럼 Web Storage 는 무엇이고 어떻게 사용하는걸까 ?

## Web Storage 를 통한 데이터 저장

우선 이 API를 이용하면 데이터가 key/value 로 저장된다.
우리가 흔히 보는 Object 로 볼 수 있고 ,
JSON으로 저장된다고 보는게 어쩌면 맞을 수 도 있겠다.

storage 객체는 페이지를 새로 렌더링을 해도 
storage 라는 공간에 저장을 해두기 때문에 데이터가 사라지지 않는다.

storage 는 두가지가 있는데,

- session Storage : 페이지 리로딩 및 복원을 포함한, 브라우저가 열려있는 한 최대한 긴 시간 동안 유지시킨다.
- local Storage : 위와 동일하나 브라우저가 닫혀도 데이터를 유지시킨다.


Storage.setItem() , Storage.getItem() 을 통해 
값을 저장하거나 불러온다.

```js
localStorage.setItem('name', 'donghyeok')
localStorage.getItem(users)
```

이렇게 저장하고 크롬 개발자도구를 이용해 Application 탭을 보면 

![](https://images.velog.io/images/tjehdgur1500/post/e00dd4a9-4482-430f-915c-a03da5bd5ea1/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-21%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2012.32.25.png)

storage 에 저장되있는 데이터말고도 방금 생성한 데이터도 들어가 있다.
이제 이 데이터들은 삭제하지 않는이상 영구적이게 된것이다.

## 객체를 저장

물론 primitive type 말고도 reference type의 자료형도 저장가능하다.
단 조금은 차이가 있다.

우선 2차원 배열 객체를 만들어서 저장시켜보자

```js
let userInfo =[
  {name : 'Kim', age : 20},
  {name : 'Park', age : 28}
]
localStorage.setItem('userInfo', userInfo)
```

이 결과는 놀랍게도 이런결과를 보여준다.

![](https://images.velog.io/images/tjehdgur1500/post/3c205826-48e1-4d96-9946-939dc9cac300/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-21%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2012.38.50.png)

object Object 에 대해 설명하고 싶지만 굉장히 딥하게 들어가야해서
이글에서 좀 벗어나게 된다.

우리는 배열객체에다가 유저정보 객체를 두개 넣었을 뿐인데 원하는 결과로 나오지 않았다.
이것을 다시 JSON이라는 형태로 변환시켜서 저장을 할 수 있다.

```js
let userInfo2 =[
  {name : 'Kim', age : 20},
  {name : 'Park', age : 28}
]
localStorage.setItem('userInfo', JSON.stringify(userInfo2))
```
![](https://images.velog.io/images/tjehdgur1500/post/88f26c61-b30b-49b8-8515-2bb8c3442fdb/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-21%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2012.46.03.png)

이제 실제 우리가 원하는 결과를 JSON으로 들어간 모습을 볼 수 있다.
현재 예시로 들기 위해 JSON 메서드를 사용하였는데 , 나중에 더 자세히 다뤄볼까 한다.

