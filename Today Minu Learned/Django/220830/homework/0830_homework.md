### 1. MTV
Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의
약자이며, 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 Django에서 하는
역할을 간략히 서술하시오.

Model - Model
Template - View
Views - Controller

1. Model
   -  데이터와 관련된 로직을 관리한다.
   -  응용프로그램의 데이터 구조를 정의하고, 데이터베이스의 기록을 관리한다.

2. Template
   -  레이아웃과 화면을 처리한다.
   -  화면상의 사용자 인터페이스 구조와 레이아웃을 정의한다.

3. Views
   -  model & template과 관련한 로직을 처리해서 응답을 반환한다.
   -  클라이언트의 요청에 대해 처리를 분기하는 역할이다.


### 2. URL
__(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을
의미한다. __(a)__는 무엇인지 작성하시오.

**Variable Routing**


### 3. Django template path
Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에
등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다.
__(a)__에 들어갈 폴더 이름을 작성하시오.

**Template**