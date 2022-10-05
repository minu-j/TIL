1. SQL 용어 및 개념

    아래의 보기에서 각 문항의 설명에 맞는 용어를 고르시오.

    **기본 키, 테이블, 스키마, 레코드, 컬럼**

    1) 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것

        > 스키마
    
    2) 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합

        > 테이블
    
    3) 고유한 데이터 형식이 지정되는 열

        > 컬럼
    
    4) 단일 구조 데이터 항목을 가리키는 행

        > 레코드
    
    5) 각 행의 고유 값

        > 기본 키

2. SQL 문법

    아래의 보기 (1) ~ (4) 중에서, DML이 아닌 것을 고르시오.

    > (1) CREATE

        (1) CREATE
        (2) UPDATE
        (3) DELETE
        (4) SELECT

3. Relational DBMS

    RDBMS의 개념적 정의와 이를 기반으로 한 DB-Engine의 종류 세가지 이상 작성하시오.

    > RDBMS는 관계형 데이터베이스 관리 시스템의 약자로, 관계형 데이터베이스를 만들고 업데이트하고 관리하는 데 사용하는 프로그램을 의미한다. 
    >
    > DB-Engine의 종류로는 SQLite, MySQL, Oracle Database, PostgreSQL, Microsoft SQL Server 등이 있다.

4. INSERT INTO

    다음과 같은 스키마를 가지는 테이블이 있을 때,
    아래의 보기 (1) ~ (4) 중 틀린 문장을 고르시오.

    ```sql
    CREATE TABLE classmates (
    name TEXT, 
    age INT,
    address TEXT
    );
    ```

    > (3)
    > 
    > 맞지 않는 문법 사용

    (1) `INSERT INTO classmates (name, age, address) VALUES('홍길동', 20, 'seoul');`

    (2) `INSERT INTO classmates VALUES('홍길동', 20, 'seoul');`

    (3) `insert into classmates values(address='seoul', age=20, name='홍길동');`

    (4) `insert into classmates (address, age, name) values('seoul', 20, '홍길동');`

5. 와일드카드 문자

    SQL에서 사용 가능한 와일드카드 문자인 %와 _을 비교하여 작성하시오.

    > '%'는 해당 위치에 있는 문자의 길이가 제한되지 않지만, '_'는 해당 위치에 1개의 문자가 위치해야 한다.