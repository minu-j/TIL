CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 값이 입력하고자 하는 필드와 위치가 서로 맞지 않아 엉뚱한 곳에 값이 추가됨.

  -- INSERT INTO zoo VALUES 
  -- (5, 180, 210, 'gorilla', 'omnivore');

  INSERT INTO zoo VALUES 
  ('gorilla', 'omnivore', 210, 180, 5);

-- 2) rowid는 UNIQUE 속성을 가지므로 중복되어 지정될 수 없음.

  -- INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
  -- (10,'dolphin', 'carnivore', 210, 3),
  -- (10, 'alligator', 'carnivore', 250, 50);

  INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
  (10,'dolphin', 'carnivore', 210, 3),
  (11, 'alligator', 'carnivore', 250, 50);

-- 3) weight는 NOT NULL 속성을 가지므로 입력되지 않을 수 없음.

  -- INSERT INTO zoo (name, eat, age) VALUES
  -- ('dolphin', 'carnivore', 3);

  INSERT INTO zoo (name, eat, weight, age) VALUES
  ('dolphin', 'carnivore', 160, 3);