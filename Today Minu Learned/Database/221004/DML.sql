-- CRUD
  -- INSERT -> C
  -- SELECT -> R
  -- UPDATE -> U
  -- DELETE -> D

-- shell - $ sqlite3

CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
  );

-- 조회
  -- Select
    SELECT first_name, age FROM users; -- 이름과 나이 조회

    SELECT * FROM users; -- 전체 데이터 조회

    SELECT rowid, first_name FROM users; -- rowid 조회

  -- Sorting rows
    SELECT first_name, age FROM users
    ORDER BY age ASC; -- 나이 오름차순으로 정렬

    SELECT first_name, age FROM users
    ORDER BY age DESC; -- 나이 내림차순으로 정렬

    SELECT first_name, age, balance FROM users
    ORDER BY age ASC, balance DESC; -- 1. 나이 오름차순, 2. 계좌 내림차순 정렬
    
    -- NULL -> 가장 작은 값으로 취급

  -- Filtering data
    -- DISTINCT : 중복 값 없이 조회하기
      SELECT DISTINCT country FROM users;

      SELECT DISTINCT country FROM users 
      ORDER BY country; -- 중복 없이 지역 내림차순으로 조회하기

      SELECT DISTINCT first_name, country FROM users; -- 이름, 지역 중복없이 조회
      
      SELECT DISTINCT first_name, country FROM users
      ORDER BY country DESC; -- 이름, 지역 중복없이 지역 내림차순 정렬

      -- NULL -> 모든 NULL을 같은 값으로 취급

    -- WHERE : 조회시 특정 검색 조건을 지정
      SELECT first_name, age, balance FROM users
      WHERE age >= 30 AND balance > 500000; -- 나이가 30살 이상이고, 계좌 잔고가 50만원 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기

    -- LIKE : 특정한 패턴 검색
      -- 패턴 구성을 위한 Wildcards character
        -- 1. % : 글자수가 정해지지 않음
        -- 2. _ : 반드시 해당 자리에 한자리가 있어야 함.

      SELECT first_name, last_name FROM users
      WHERE first_name LIKE '%호%'; -- 이름에 '호'가 포함되는 사람의 이름과 성 조회

      SELECT first_name, last_name FROM users
      WHERE first_name LIKE '%준'; -- 이름이 '준'으로 끝나는 사람의 이름과 성 조회

      SELECT first_name, phone FROM users
      WHERE phone LIKE '02-%'; -- 서울지역 전화번호를 가진 사람들의 이름과 전화번호 조회

      SELECT first_name, age FROM users
      WHERE age LIKE '2_'; -- 나이가 20대인 사람들의 이름과 나이 조회

      SELECT first_name, phone FROM users
      WHERE phone LIKE '%-51__-%'; -- 전화번호 중간 네자리가 51로 시작되는 사람 조회

    -- IN : 값이 값 목록 결과에 있는 값과 일치하는지 확인
      SELECT first_name, country FROM users
      WHERE country IN ('경기도', '강원도'); -- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회

    -- BETWEEN : 값이 값 범위에 있는지 테스트
      SELECT first_name, age FROM users
      WHERE age BETWEEN 20 and 30; -- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이

      SELECT first_name, age FROM users
      WHERE age NOT BETWEEN 20 and 30; -- 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름과 나이
      
    -- LIMIT : 결과에서 행 수 제한
      SELECT first_name, balance FROM users
      ORDER BY balance DESC
      LIMIT 10; -- 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고

      SELECT first_name, age FROM users
      ORDER BY age ASC
      LIMIT 5; -- 나이가 가장 어린 다섯명

    -- OFFSET : limit와 함께 사용하여 특정 지정된 위치부터의 데이터를 조회
      SELECT first_name, age FROM users
      ORDER BY age ASC
      LIMIT 5 OFFSET 5; -- 나이가 가장 어린 다섯명을 다섯번째부터 조회(6~10번)

    -- GROUP BY : 특정 그룹으로 묶인 결과를 출력
      SELECT country, COUNT(*) FROM users
      GROUP BY country; -- 각 지역별로 몇명이 거주하는지 출력

      -- Agregate function : 집계 함수
        -- AVG(), COUNT(), MAX(), MIN(), SUM()

      SELECT COUNT(*) FROM users;-- users 테이블의 전체 행 수 출력

      SELECT AVG(age) FROM users
      WHERE age >= 30; -- 나이가 30살 이상인 사람들의 평균 나이 출력

      SELECT last_name, COUNT(*) AS number_of_name FROM users
      GROUP BY last_name; -- 각 성씨별 사람 수 출력
      
       -- AS 키워드 : 컬럼 이름을 임시적으로 변경하여 조회할 수 있음

-- CRUD
  -- Create
    -- INSERT : 새 행을 테이블에 삽입
    INSERT INTO
    
    -- UPDATE : 기존 행의 데이터를 업데이트
    UPDATE SET / WHERE

    -- DELETE : 테이블에서 행을 제거
    DELETE FROM / WHERE