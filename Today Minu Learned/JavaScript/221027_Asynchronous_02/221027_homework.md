1. True, True, True

2. 1. Call Stack : 'Hello SSAFY!' 출력 처리
    2. Call Stack : setTimeout이 바로 처리 불가하므로 Web API로 넘기기
    3. Call Stack : 'Bye SSAFY!' 출력 처리  
        Web API : setTimeout 처리 후 Tast Queue로 넘기기
    4. Event Loop : Call Stack이 비어있는지 확인 후 Task Queue에 있는 setTimeout Call Stack으로 넘기기
    5. Call Stack : 'I am from setTimeout' 출력 처리