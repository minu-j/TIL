1. True, False

2. - 동기식 코드 : 위에서부터 순서대로 처리가 된다.
    - 비동기식 코드 : 즉시 처리 가능한 작업은 즉시 처리하고, 오래 걸리는 작업은 요청을 보내놓고 기다리지 않고 다음 코드로 진행 한다.

3. ```javascript
    axios.get('https://api.example.com/data')
        .then(function (response) {
            console.log(response.data)
        })
    ```