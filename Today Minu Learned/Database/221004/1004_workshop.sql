-- 1) countries 테이블을 생성하시오.
CREATE TABLE countries (
  room_num TEXT,
  check_in TEXT,
  check_out TEXT,
  grade TEXT,
  price INTEGER
  );

-- 2) 데이터를 입력하시오.
INSERT INTO countries
VALUES 
  ('B203', '2019-12-31', '2020-01-03', 'suite', 900),
  ('1102', '2020-01-04', '2020-01-08', 'suite', 850),
  ('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
  ('807', '2020-01-04', '2020-01-07', 'superior', 300);

-- 3) 테이블의 이름을 hotels로 변경하시오.
ALTER TABLE countries
RENAME TO hotels;

-- 4) 객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num과 price를 조회하시오.
SELECT room_num, price FROM hotels
ORDER BY price DESC
LIMIT 2;

-- 5) grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오.
SELECT grade, COUNT(*) AS count_grade FROM hotels
GROUP BY grade
ORDER BY count_grade DESC;

-- 6) 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보를 조회하시오.
SELECT * FROM hotels
WHERE room_num LIKE 'B%' OR grade IN ('deluxe');


-- 7) 지상층 객실이면서 2020년 1월 4일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오.
SELECT room_num, price FROM hotels
WHERE room_num NOT LIKE 'B%' and check_in IN ('2020-01-04');