// matcher

// 일치 비교
test('1은 1이다.', () => {
  expect(1).toBe(1);
});

test('1은 2가 아니다', () => {
  expect(1).not.toBe(2);
});

// test('객체 비교', () => {
//   expect({ name: 'jung', age: 26 }).toBe({ name: 'jung', age: 26 });
// });
// If it should pass with deep equality, replace "toBe" with "toStrictEqual"

test('깊은 비교를 위해서는 toEqual을 사용한다.', () => {
  expect({ name: 'jung', age: 26 }).toEqual({ name: 'jung', age: 26 });
});

test('toEqual은 undefined 체크를 하지 않는다.', () => {
  expect({ name: 'jung', age: 26, hight: undefined }).toEqual({ name: 'jung', age: 26 });
});

test('toStrictEqual은 엄격하게 객체를 체크한다.', () => {
  expect({ name: 'jung', age: 26, hight: 180 }).toStrictEqual({ name: 'jung', age: 26, hight: 180 });
});

// check null
test('null은 null이다.', () => {
  expect(null).toBeNull();
});

// check undefined
test('undefined는 undefined이다.', () => {
  expect(undefined).toBeUndefined();
});

test('1은 undefined가 아니다.', () => {
  expect(1).toBeDefined();
});

// boolean
test('1은 true이다', () => {
  expect(1).toBeTruthy();
});

test('0은 false이다', () => {
  expect(0).toBeFalsy();
});

test('숫자의 크기 비교', () => {
  // 2 > 1
  expect(2).toBeGreaterThan(1);
  // 2 >= 1
  expect(2).toBeGreaterThanOrEqual(1);
  // 1 < 2
  expect(1).toBeLessThan(2);
  // 1 <= 2
  expect(1).toBeLessThanOrEqual(2);
  // 1 == 1
  expect(1).toBe(1);
  expect(1).toEqual(1);
});

test('부동소수점 문제 해결법', () => {
  // expect(0.1 + 0.2).toBe(0.3);
  // Expected: 0.3
  // Received: 0.30000000000000004
  expect(0.1 + 0.2).toBeCloseTo(0.3);
});

test('정규표현식으로 문자열 판단', () => {
  expect('Hello World').toMatch(/H/);
  expect('Hello World').toMatch(/h/i);
});

test('배열의 Value 포함여부', () => {
  expect(['A', 'B', 'C']).toContain('A');
});

test('에러 발생 테스트', () => {
  expect(() => {
    throw new Error('x');
  }).toThrow('x');
});
