// async

// callback 패턴
const getCallbackTrue = (callback: any) => {
  setTimeout(() => {
    callback(true);
  }, 3000);
};

// test('3초 뒤 오류를 내야하는데 테스트가 그냥 끝남', () => {
//   getName((isTrue: boolean) => {
//     expect(isTrue).toBeFalsy();
//   });
// });

test('3초 뒤 true를 받아옴', done => {
  getCallbackTrue((isTrue: boolean) => {
    expect(isTrue).toBeTruthy();
    done(); // done 함수를 호출하지 않으면 비동기 함수가 끝나기 전에 테스트를 종료해버림.
  });
});

// test('done을 실행하지 않으면 timeout 오류', done => {
//   getName((isTrue: boolean) => {
//     expect(isTrue).toBeTruthy();
//   });
// });
// thrown: "Exceeded timeout of 10000 ms for a test while waiting for `done()` to be called.

// const getNameError = (callback: any) => {
//   setTimeout(() => {
//     throw new Error('에러발생');
//   }, 3000);
// };

// test('비동기 에러 catch', done => {
//   getNameError((isTrue: boolean) => {
//     try {
//       expect(isTrue).toBeTruthy();
//       done();
//     } catch (error) {
//       done();
//     }
//   });
// });

// Promise를 return하는 비동기 함수
const getPromiseTrue = () =>
  new Promise((res, rej) => {
    setTimeout(() => {
      res(true);
    }, 3000);
  });

test('promise 값 테스트', () =>
  getPromiseTrue().then(() => {
    expect(true).toBeTruthy();
  }));

// resolves, rejects를 이용해 작성할 수 있는 같은 코드
test('비동기 에러 catch', () => expect(getPromiseTrue()).resolves.toBeTruthy());

const getPromiseError = () =>
  new Promise((res, rej) => {
    setTimeout(() => {
      rej('에러 발생');
    }, 3000);
  });

test('promise 값 테스트', () =>
  getPromiseError()
    .then(() => {
      expect(true).toBeTruthy();
    })
    .catch(e => {}));

// resolves, rejects를 이용해 작성할 수 있는 같은 코드
test('비동기 에러 catch', () => expect(getPromiseError()).rejects.toBeTruthy());
