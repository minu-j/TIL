1. `True`, `True`

2. - click : 포인팅 장치 버튼(모든 버튼; 주 버튼만 해당될 예정)이 엘리먼트에서 눌렸다가 놓였을 때.
    - mouseover : 포인팅 장치가 리스너가 등록된 엘리먼트나 그 자식 엘리먼트의 위로 이동했을 때.
    - mouseout : 포인팅 장치가 리스너가 등록된 엘리먼트 또는 그 자식 엘리먼트의 밖으로 이동했을 때.
    - keydown : 키가 눌렸을 때
    - keyup : 키 누름이 해제될 때
    - load : 진행이 성공했을 때.
    - scroll : 다큐먼트 뷰나 엘리먼트가 스크롤되었을 때.
    - change : \<input>, \<select>, 엘리먼트에 change 이벤트가 발생하거나, \<textarea> 엘리먼트의 value에 변화가 생겼을 때
    - input : \<input>, \<select>, 엘리먼트에 input 이벤트가 발생하거나, \<textarea> 엘리먼트에 변화가 생겼을 때

3. ```javascript
    const button document.querySelector('button')

    button.addEventListener('click', function () {
        console.log('button clicked!')
    })
    ```