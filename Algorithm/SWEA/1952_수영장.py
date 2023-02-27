def planing(plan, month):
    global cost
    global min_cost

    if month >= 13:  # 13월이 되면 종료
        if cost < min_cost:  # 최저값보다 더 저렴하면 최저값 대치
            min_cost = cost
        return

    if plan[month] == 0:  # 해당 월에 이용계획이 없다면 패스
        planing(plan, month + 1)

    else:  # 이용계획이 있다면?

        # 하루짜리 구매시 이용일수 x 하루 요금 비용에 합한 후 다음달로
        cost += plan[month] * one_day
        if cost < min_cost:  # 더한 값이 최소비용보다 크면 다음 재귀 가지도 마
            planing(plan, month + 1)
        cost -= plan[month] * one_day

        # 한달짜리 구매시 한달 요금 비용에 합한 후 다음달로
        cost += one_month
        if cost < min_cost:
            planing(plan, month + 1)
        cost -= one_month

        # 세달짜리 구매시 세달 요금 비용에 합한 후 세달 뒤로
        cost += three_month
        if cost < min_cost:
            planing(plan, month + 3)
        cost -= three_month


for tc in range(int(input())):
    one_day, one_month, three_month, year = map(int, input().split())
    year_plan = [0] + list(map(int, input().split())) + [0, 0]

    cost = 0
    min_cost = year  # 제일 적은 경우는 일단 1년짜리 샀을 때로 가정하기
    planing(year_plan, 1)

    print(f'#{tc + 1} {min_cost}')