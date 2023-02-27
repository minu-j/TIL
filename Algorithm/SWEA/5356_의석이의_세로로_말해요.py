for tc in range(int(input())):
    word = [input() for _ in range(5)]

    print(f'#{tc + 1}', end=' ')   # 테스트케이스 번호 출력
    for i in range(15):
        for j in range(5):
            print(word[j][i:i + 1], end='')   # 가로 15, 세로 5번을 돌면서 띄어쓰기 없이 출력
    print('')