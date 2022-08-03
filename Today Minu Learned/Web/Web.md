# HTML & CSS



## Web이란?

### 웹사이트의 구성요소

1. HTML : 구조
2. CSS : 표현
3. Javascript : 동작



### 웹 표준

* 웹에서 표준적으로 사용되는 기술이나 규칙
* 어떤 브라우저든 웹페이지가 동일하게 보이도록 함 -> 크로스 브라우징

http://caniuse.com



---



## HTML

: **Hyper Text** Markup Language

- Hyper Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어(HTML, Markdown 등)



## HTML의 기본 구조

* html : 문서의 최상위(root) 요소

* head : 문서 메타데이터 요소 - 일반적으로 브라우저에 나타나지 않는 내용
  
  * 문서 제목, 인코딩, 스타일, 외부파일 로딩 등
  
  * 예시
    
    ```html
    <title></title>  : 브라우저 상단 타이틀
    <meta>  : 문서 레벨 메타데이터 요소
    <link>  : 외부 리소스 연결 요소(CSS파일, favicon 등)
    <script></script> : 스크립트 요소(JavaScript 파일/코드)
    <style></style> : CSS 직접 작성
    ```
  
  * Open Graph Protocol : 메타데이터를 표현하는 새로운 규약

* body : 문서 본문 요소 - 실제 화면 구성과 관련된 내용



### 요소(element)

```html
<시작태그>내용</종료태그>
```

* 시작태그 / 내용 / 종료태그 : 내용이 없는 태그들도 존재(닫는 태그가 없음)
* 요소는 중첩될 수 없음. : 오류가 발생하는 것이 아닌, 깨져서 출력되므로 주의가 필요함



### 속성(attribute)

```html
<a href="https://google.com"></a>
```

* 속성을 통해 태그의 부가적인 정보를 설정

* 요소는 속성을 가질 수 있으며, 경로나 크기

* HTML Global Attribute : 모든 HTML요소가 공통으로 사용할 수 있는 대표적인 속성
  
  * id : 문서 전체에서 유일한 고유 식별자 지정
  * class : 공백으로 구분된 해당 요소의 클래스의 목록(css, js에서 요소를 선택하거나 접근)
  * data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
  * style : inline 스타일
  * title : 요소에 대한 추가 정보 지정
  * tabindex : 요소의 탭 순서

* 주석
  
  ```html
  <!-- 주석내용 -->
  ```



### 시맨틱 태그

HTML태그가 특정 목적, 역할 및 의미적 가치(semantic value)를 가지는 것

* sementic tag
  * header : 문서 전체나 섹션의 헤더(머리말 부분)
  * nav : 내비게이션
  * aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  * section : 문서의 일반적인 구분, 콘텐츠의 그룹을 표현
  * article : 문서 페이지, 사이트 안에서 독립적으로 구분되는 영역
  * footer : 문서 전체나 섹션의 푸터(마지막 부분)
* 시맨틱 태그를 사용하는 이유 : 검색엔진 등에 의미있는 정보의 그룹을 태그로 표현
* non semantic 요소
  * div, span
  
  

### 렌더링

렌더링 : 쓰여진 코드를 웹사이트 형태로 표시하는 방법

* DOM(Document object model)트리



## HTML 문서 구조화

### 텍스트 요소

```html
<a></a> : href속성을 활용하여 다른 url로 연결하는 하이퍼링크 생성
<b></b> : 굵은 글씨 요소
<strong></strong> : 중요한 강조하고자 하는 요소(보통 굵은 글씨로 표현)
<i></i> : 기울임 글씨 요소
<em></em> : 중요한 강조하고자 하는 요소(보통 기울임 글씨로 표현)
<br> : 텍스트 내에 줄바꿈 생성
<img> : src속성을 활용하여 이미지 표현
<span></span> : 의미없는 인라인 컨테이너
```

### 그룹 컨텐츠

```html
<p>
  </p> : 하나의 문단(paragraph)
<hr> : 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표시됨(a horizontal rule)
<ol>
  </ol> : 순서가 있는 리스트(ordered)
<ul>
  </ul> : 순서가 없는 리스트(unordered)
<pre></pre> : HTML에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백문자를 유지
<blockquote>
  </blockquote> : 텍스트가 긴 인용문. 주로 들여쓰기를 한 것으로 표현됨.
<div>
  </div> : 의미없는 블록 레벨 컨테이너
```

### form

* <form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
  
  ```html
  <form action="/search" method="GET">
  </form>
  ```

* <form>의 기본 속성
  
  * action : form을 처리할 서버의 URL(데이터를 보낼 곳)
  
  * method : form을 제출할 때 사용할 http메서드(get 혹은 post)
  
  * enctype : method가 post인 경우 데이터의 유형
    
    * application/x-www-form-urlencoded : 기본값
    
    * multipart/form-data : 파일 전송시 input type이 file인 경우)
    
    * text/plain : HTML5 디버깅용(잘 사용되지 않음)
    
    

### input

* 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

* <input> 대표적인 속성
  
  * name : form control에 적용되는 이름(이름/값 페어로 전송됨)
  
  * value : form control에 적용되는 값(이름/값 페어로 전송됨)
  
  * required, readonly, autofocus, autocomplete, disable 등
  
  * input label : label을 클릭하여 input자체의 초점을 맞추거나 활성화시킬 수 있음.
    
    * <input>에 id속성을, <label>에는 for 속성을 활용하여 상호 연관을 시킴.

* input 유형
  
  * 일반
    
    * text : 일반 텍스트 입력
    
    * password : 입력시 값이 보이지 않고 문자를 특수기호로 표현
    
    * email : 이메일 형식이 아닌 경우 form 제출 불가
    
    * number : min, max, step속성을 활용하여 숫자 범위 설정 가능
    
    * file : accept 속성을 활용하여 파일 타입 지정 가능
  
  * 항목 중 선택
    
    * checkbox : 다중 선택
    
    * radio : 단일 선택
  
  * 기타
    
    * color : color picker
    
    * date : date picker
    
    * hidden : 사용자에게 보이지 않는 input



---



## CSS

CSS(Cascading Style Sheets) : 스타일을 지정하기 위한 언어

```css
h1 {
  color: blue;
  font-size: 15px;
}
```

### css 정의 방법

* 인라인(inline) 

* 내부참조(embedding) - <style>

* 외부참조(link file) - 분리된 CSS파일



### 선택자(selector)

* 기본 선택자
  
  * 전체 선택자
  
  * 요소 선택자 : HTML태그를 직접 선택
  
  * 클래스 선택자 : 마침표 문자로 시작하며 해당 클래스가 적용된 항목을 선택
  
  * 아이디 선택자 : # 으로 시작하며, 해당 아이디가 적용된 항목을 선택

* 결합자(combinators)
  
  * 자손 결합자(공백) : selectorA 하위의 모든 selectorB 요소
  
  * 자식 결합자 : selectorA 바로 아래의 selectorB 요소
  
  * 일반 형제 결합자
  
  * 인접 형제 결합자

* 의사 클래스/요소(Pseudo class)
  
  * 링크, 동적 의사 클래스
  
  * 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
  
  
  
  ### CSS 적용 우선순위
  
  1. 중요도(importance)
  
  2. 우선순위(specificity)
     
     * 범위가 좁을 수록 우선 적용된다.
  
  3. CSS 파일 로딩 순서
  
  
  
  ### CSS 상속
  
  CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
  
  * 상속 되는 것, 되지 않는 것이 있다...
  
  
  
  ### CSS 기본 스타일
  
  * 크기 단위
    
    * 픽셀 : 고정적인 단위
    
    * % : 백분율 단위(가변적인 레이아웃)
    
    * em : 상속의 영향을 받으며, 배수단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
    
    * rem : 상속의 영향을 받지 않으며, 최상위 요소의 사이즈를 기준으로 배수 단위를 가짐
    
    * viewport : 디바이스의 viewport(유저 디바이스의 화면)를 기준으로 상대적인 사이즈가 결정됨.
      
      * vw, vh, vmin, vmax
  
  * 색상 단위
    
    * 색상 키워드 : red, blue, black 등
    
    * RGB : 16진수 또는 함수형 표기법을 사용
    
    * HSL : 색상, 채도, 명도를 통해 특정 색을 표현
  
  * CSS 문서표현
    
    * 텍스트 : 서체, 서체스타일, 자간, 단어간격, 행간
    
    * 컬러, 배경
    
    * 기타 : 목록, 표
    
    

### CSS Box Model

모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.

* 구성
  
  1. margin : 테두리 바깥의 외부 여백, 배경색 지정 불가능
     
     ```css
     .margin {
      margin-top: 10px;
      margin-right: 10px;
      margin-bottom: 10px;
      margin-left: 10px;
     }
     ```
  
  2. border : 테두리 영역
     
     ```css
     .boader {
      margin: 10px;
      border-width: 2px;
      border-style: dashed;
      border-color: black;
     }
     ```
  
  3. padding : 테두리 안족의 내부여백 요소에 적용된 배경색, 이미지는 padding까지 적용
     
     ```css
     .margin-padding {
      margin: 10px;
      padding: 30px;
     }
     ```
  
  4. content : 그링나 이미지 등 요소의 실제 내용
  
  

### CSS Display

* display: block
  
  * 줄바꿈이 일어나는 요소
  
  * 화면크기 전체의 가로폭을 차지한다.
  
  * 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.

* display: inline
  
  * 줄바꿈이 일어나지 않는 행의 일부 요소
  
  * content 너비만큼 가로 폭을 차지
  
  * width, height, margin-top, margin-bottom을 지정할 수 없다.
  
  * 상하 여백은 line-height로 지정한다.

* 블록 레벨 요소와 인라인 레벨 요소
  
  * 블록 : div, ul, ol, li, p, hr, form 등
  
  * 인라인 : span, a, img, input, label, b, em, i, strong 등

* display: inline-block

* display: None



### CSS Position

문서상에서 요소의 위치를 지정

1. static : 모든 태그의 기본 값(기준 위치)
* 좌표 프로퍼티(top, bottom, lest, right)를 사용하여 이동 가능한 것
  
  2. relative : 상대위치
  
  3. absolute : 절대위치
  
  4. fixed : 고정위치
  
  5. sticky : 스크롤에 따라 static -> fixed로 변경


### CSS Layout
: css layout techniques
  
  * Display

  * Position

  * Float(CSS1, 1996)

  * Flexbox(2012)

  * Grid(2017)

  * 기타(반응형 웹...)


### Normal Flow
 : inline(좌->우), block(상->하)로 쌓인다


### Float
: Float 요소를 중심으로 텍스트를 감싸게 배치하게 함.

  * none : 기본값

  * left : 요소를 왼쪽으로 띄움

  * right : 요소를 오른쪽으로 띄움


### Flexbox

CSS Flexible Box Layout : 행과 열 형태로 아이템을 배치하는 1차원 레이아웃 모델

* 축

  * main axis(메인 축)

  * cross axis(교차 축 - main axis의 수직방향)

* 구성요소

  * Flex Container(부모요소) : 부모 요소에 display: flex

  * Flex Item(자식요소)

* inline flex : Flex 내에서 인라인 요소

* 속성

  * 배치 설정

    * flex-direction : main axis 기준 방향 설정

      1. row(-reverse)

      2. column(-reverse)

    * flex-wrap : 아이템이 컨테이너 영역을 벗어나는 경우 해당 영역 내에 배치되도록 설정

      1. wrap(-reverse)

      2. nowrap

  * 공간 나누기

    * justify-content(main axis) / align-content(cross axis)

      1. flex-start

      2. flex-end
      
      3. center
      
      4. space-between
      
      5. space-around
      
      6. space-evenly

  * 정렬

    * align-items : 모든 아이템을 cross axis 기준으로 정렬
      
      1. stretch
      
      2. flex-start
      
      3. flex-end
      
      4. center
      
      5. baseline

    * align-self : 개별 아이템을 cross axis 기준으로 정렬

      1. stretch

      2. flex-start
      
      3. flex-end
      
      4. center
    
  * 기타 속성

    * flex-grow : 남은 영역을 아이템에 분배

    * order : 배치 순서

## Bootstrap

### CDN

Content Delivery Network

```css
<head>
<link href="jsdelivr link">
</head>
<body>
<script src="jsdelivr link">
</body>
```

### spacing(margin and padding)

{property}{sides}-{size} mt-3

```html
<div class="mt-3 ms-5">bootstrap-spacing</div>
```
* property : m (margin) / p (padding)

* sides : t (top) / b (bottom) / s (start) / e (end) / x (left and right) / y (top and bottom) / blank (all)

* size : 0~5 / auto

### color

```html
<div class="text(bg)-primary">
<div class="text(bg)--secondary">
<div class="text(bg)-success">
<div class="text(bg)-info">
<div class="text(bg)-warning">
<div class="text(bg)-danger">
<div class="text(bg)-light">
<div class="text(bg)-dark">
```

### text

### display

### position

### button

### dropdown

### Grid system(web design)

bootstrap grid system

* 12개의 column

* 6개의 grid breakpoint(화면크기에 따라 표시할 양을 정하는 분기점)

  ```css
  .col-{breakpoint}-
  ```

  xs - sm - md - lg - xl - xxl