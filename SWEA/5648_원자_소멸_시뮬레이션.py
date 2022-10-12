for tc in range(int(input())):
    N = int(input())

    atom = []
    for _ in range(N):
        atom.append([_] + list(map(int, input().split())))

    crush = []

    for num1, x1, y1, d1, e1 in atom:
        t = 0   # 부딪칠때까지 걸리는 시간

        if d1 == 1 or d1 == 3:

            # 해당 원자와 다른 원자를 확인
            for num2, x2, y2, d2, e2 in atom:
                # 아래로 직진하는 원자의 경우
                if d1 == 1:
                    # x 좌표가 같으면서 위로 직진하는 원자와 부딪친다.
                    if d2 == 0 and x1 == x2:
                        # 부딪치는 시간은 거리의 1/2가 될 것임.
                        t = abs(y1 - y2) / 2
                        crush_case = (t, min(num1, num2), max(num1, num2))
                        if crush_case not in crush:
                            crush.append(crush_case)
                        continue

                    # 또는 수직이동하면서, x, y의 거리가 같다면 부딪친다.
                    elif d2 == 2 or d2 == 3:
                        if abs(x1 - x2) == abs(y1 - y2):
                            # 부딪치는 시간은 수직 거리가 될 것임.
                            t = abs(y1 - y2)
                            crush_case = (t, min(num1, num2), max(num1, num2))
                            if crush_case not in crush:
                                crush.append(crush_case)
                            continue

                # 오른쪽으로 직진하는 원자의 경우
                if d1 == 3:
                    # y 좌표가 같으면서 왼쪽으로 직진하는 원자와 부딪친다.
                    if d2 == 2 and y1 == y2:
                        # 부딛치는 시간은 거리의 1/2가 될 것임.
                        t = abs(x1 - x2) / 2
                        crush_case = (t, min(num1, num2), max(num1, num2))
                        if crush_case not in crush:
                            crush.append(crush_case)
                        continue

                    # 또는 수직이동하면서, x, y의 거리가 같다면 부딪친다.
                    elif d2 == 0 or d2 == 1:
                        if abs(x1 - x2) == abs(y1 - y2):
                            # 부딪치는 시간은 수직 거리가 될 것임.
                            t = abs(y1 - y2)
                            crush_case = (t, min(num1, num2), max(num1, num2))
                            if crush_case not in crush:
                                crush.append(crush_case)
                            continue

    # 충돌이 한번도 없다면 0 출력 후 종료
    if not crush:
        print(f'#{tc + 1} 0')
        continue

    # 충돌이 있다면?
    else:
        live_atom = list(range(N))
        energy = 0
        crush.sort()

        before_t = crush[0][0]
        crush_atoms = set()

        for t, atom1, atom2 in crush:
            if t == before_t:
                if atom1 in live_atom and atom2 in live_atom:
                    crush_atoms.add(atom1)
                    crush_atoms.add(atom2)
            else:
                for a in crush_atoms:
                    live_atom.remove(a)
                crush_atoms = set()
                before_t = t
                if atom1 in live_atom and atom2 in live_atom:
                    crush_atoms.add(atom1)
                    crush_atoms.add(atom2)

        for a in crush_atoms:
            energy += atom[a][4]
            live_atom.remove(a)

        print(f'#{tc + 1} {energy}')
