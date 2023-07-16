let num = 0;

// 모든 테스트 이전 콜백 실행
beforeAll(() => {});

// 각 테스트 이전에 콜백 실행
beforeEach(() => {
  num = 0;
});

// 모든 테스트 이후 콜백 실행
afterAll(() => {});

// 각 테스트 직후 콜백 실행
afterEach(() => {});

describe('작업 묶음', () => {
  test('0 + 0 = 0', () => {
    num = num + 0;
    expect(num).toBe(0);
  });
  test('0 + 1 = 1', () => {
    num = num + 1;
    expect(num).toBe(1);
  });

  // skip메서드를 붙히면 해당 테스트 skip
  test.skip('0 + 2 = 2', () => {
    num = num + 2;
    expect(num).toBe(2);
  });
  // only메서드를 붙히면 다른 테스트 skip
  test.only('0 + 3 = 3', () => {
    num = num + 3;
    expect(num).toBe(3);
  });
});
