for tc in range(int(input())):
    N = int(input())

    atom = []
    for _ in range(N):
        atom.append([_] + list(map(int, input().split())))

    crush = []

    for num1, x1, y1, d1, e1 in atom:
        t = 0   # 부딪칠때까지 걸리는 시간

        if d1 == 0 or d1 == 1 or d1 == 3:

            # 해당 원자와 다른 원자를 확인
            for num2, x2, y2, d2, e2 in atom:

                # 아래로 직진하는 원자의 경우
                if d1 == 1:
                    # x 좌표가 같으면서 부딪힐 수 있는 범위로 움직이며, 위로 직진하는 원자와 부딪친다.
                    if d2 == 0 and x1 == x2 and y1 > y2:
                        # 부딪치는 시간은 거리의 1/2가 될 것임.
                        t = abs(y1 - y2) / 2
                        crush_case = (t, min(num1, num2), max(num1, num2))
                        if crush_case not in crush:
                            crush.append(crush_case)
                        continue

                    # 또는 수직이동하면서, 부딪힐 수 있는 범위로 움직이며, x, y의 거리가 같다면 부딪친다.
                    elif d2 == 2 and y1 > y2 and x1 < x2 or d2 == 3 and y1 > y2 and x1 > x2:
                        if abs(x1 - x2) == abs(y1 - y2):
                            # 부딪치는 시간은 수직 거리가 될 것임.
                            t = abs(y1 - y2)
                            crush_case = (t, min(num1, num2), max(num1, num2))
                            if crush_case not in crush:
                                crush.append(crush_case)
                            continue

                # 위로 직진하는 원자의 경우
                elif d1 == 0:
                    # 정면 충돌은 아래로 직진하는 경우와 중복됨.
                    # 수직이동하면서, 부딪힐 수 있는 범위로 움직이며, x, y의 거리가 같다면 부딪친다.
                    if d2 == 2 and y1 < y2 and x1 < x2 or d2 == 3 and y1 < y2 and x1 > x2:
                        if abs(x1 - x2) == abs(y1 - y2):
                            # 부딪치는 시간은 수직 거리가 될 것임.
                            t = abs(y1 - y2)
                            crush_case = (t, min(num1, num2), max(num1, num2))
                            if crush_case not in crush:
                                crush.append(crush_case)
                            continue

                # 오른쪽으로 직진하는 원자의 경우
                elif d1 == 3:
                    # y 좌표가 같으면서, 부딪힐 수 있는 범위로 움직이며, 왼쪽으로 직진하는 원자와 부딪친다.
                    if d2 == 2 and y1 == y2 and x1 < x2:
                        # 부딛치는 시간은 거리의 1/2가 될 것임.
                        t = abs(x1 - x2) / 2
                        crush_case = (t, min(num1, num2), max(num1, num2))
                        if crush_case not in crush:
                            crush.append(crush_case)
                        continue

                    # 또는 수직이동하면서, 부딪힐 수 있는 범위로 움직이며, x, y의 거리가 같다면 부딪친다.
                    elif d2 == 0 and x1 < x2 and y1 > y2 or d2 == 1 and x1 < x2 and y1 < y2:
                        if abs(x1 - x2) == abs(y1 - y2):
                            # 부딪치는 시간은 수직 거리가 될 것임.
                            t = abs(y1 - y2)
                            crush_case = (t, min(num1, num2), max(num1, num2))
                            if crush_case not in crush:
                                crush.append(crush_case)
                            continue

                # 왼쪽으로 직진하는 원자의 경우는 다른 모든 경우에 포함됨.

    # 충돌이 한번도 없다면 0 출력 후 종료
    if not crush:
        print(f'#{tc + 1} 0')
        continue

    # 충돌이 있다면?
    else:
        not_crush_atom = list(range(N))     # 아직 충돌 안해서 살아있는 원자
        energy = 0                          # 에너지 합
        crush.sort()                        # 정렬한 충돌 케이스들
        before_t = crush[0][0]              # 첫번째 비교용 변수
        crush_atoms = set()                 # 충돌한 원자들 모으기

        # 충돌 케이스를 돌면서, 같은 시간에 충돌한 애들을 한 셋에 모아서 충돌 안한 원자 리스트에서 삭제하고 에너지 더하기
        for t, atom1, atom2 in crush:
            if t == before_t:   # 이전 충돌과 동일 시간이면서,
                if atom1 in not_crush_atom and atom2 in not_crush_atom:   # 원자 둘다 살아있다면
                    crush_atoms.add(atom1)      # 충돌한 원자 셋에 모으기
                    crush_atoms.add(atom2)
            else:       # 시간이 다르다면
                for a in crush_atoms:   # 충돌한 원자들 정리하고 에너지 값 더하기
                    energy += atom[a][4]
                    not_crush_atom.remove(a)
                crush_atoms = set()
                before_t = t   # 시간도 조정하고

                # 다시 충돌 셋 모으기
                if atom1 in not_crush_atom and atom2 in not_crush_atom:
                    crush_atoms.add(atom1)
                    crush_atoms.add(atom2)

        # 다 끝나면 가장 늦게 충돌한 원자들 정리하기
        for a in crush_atoms:
            energy += atom[a][4]
            not_crush_atom.remove(a)
        crush_atoms = set()
        
        print(f'#{tc + 1} {energy}')
