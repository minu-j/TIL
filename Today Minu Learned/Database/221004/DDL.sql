-- 테이블 생성

CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);

-- 테이블 수정

  ALTER TABLE contacts
  RENAME TO new_contacts; -- 테이블 이름 바꾸기

  ALTER TABLE new_contacts 
  RENAME COLUMN name TO last_name; -- 컬럼 이름 바꾸기

  ALTER TABLE new_contacts
  ADD COLUMN address TEXT NOT NULL; -- 컬럼 추가하기(기존 데이터가 있을 경우 기본데이터를 지정하지 않으면 not null 불가)

  ALTER TABLE new_contacts
  DROP COLUMN address; -- 컬럼 삭제(PK, UNIQUE 등 삭제 불가)

-- 테이블 삭제

  DROP TABLE new_contacts;