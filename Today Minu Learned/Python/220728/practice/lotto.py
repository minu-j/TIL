# 여기에 필요한 모듈을 추가합니다.
import random
import json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        self.lines = []
        for i in range(n):
            line = []
            while int(len(line)) <= 6:
                num = random.randint(1, 45)
                if num in line:
                    pass
                else:
                    line.append(num)
                line.sort()
            self.number_lines.append(line)

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        self.draw_number = draw_number
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        lotto = json.load(lotto_json)
        Lotto.year = lotto['drwNoDate'][0:4]
        Lotto.month = lotto['drwNoDate'][5:7]
        Lotto.day = lotto['drwNoDate'][8:]
        print('=========================================')
        print(f'              제 {self.draw_number}회 로또')
        print('=========================================')
        print(f'추첨일 : {Lotto.year}/{Lotto.month}/{Lotto.day} (토)')
        print('=========================================')
        for i in range(len(self.number_lines)):
            abc = ['A', 'B', 'C', 'D', 'E']
            print(f'{abc[i]} : {self.number_lines[i]}')

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        self.draw_number = draw_number
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        lotto = json.load(lotto_json)
        self.main_numbers = [lotto['drwtNo1'], lotto['drwtNo2'], lotto['drwtNo3'], lotto['drwtNo4'], lotto['drwtNo5'], lotto['drwtNo6']]
        self.bonus_number = lotto['bnusNo']
        
        print('=========================================')
        print(f'당첨 번호 : {self.main_numbers} + {self.bonus_number}')
        print('=========================================')

        for i in range(len(self.number_lines)):
            self.same_main_count = 0
            self.is_bonus = False
            abc = ['A', 'B', 'C', 'D', 'E']

            for _ in range(len(self.number_lines)):
                if self.number_lines[i][_] in self.main_numbers:
                    self.same_main_count += 1

                if self.number_lines[i][_] == self.bonus_number:
                    self.is_bonus = True

            if self.same_main_count == 6:
                self.ranking = 1
            elif self.same_main_count == 5:
                if self.is_bonus == True:
                    self.ranking = 2
                else:
                    self.ranking = 3
            elif self.same_main_count == 4:
                self.ranking = 4
            elif self.same_main_count == 3:
                self.ranking = 5
            else:
                self.ranking = -1
                
            if self.is_bonus == True:
                self.bonus = ' + 보너스 일치'
            else:
                self.bonus = ' 일치'

            if self.ranking == -1:
                self.ranking_word = '낙첨'
            else:
                self.ranking_word = f'{self.ranking}등 당첨!'

            print(f'{abc[i]} : {self.same_main_count}개{self.bonus} ({self.ranking_word})')

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        lotto = json.load(lotto_json)
        year = lotto['drwNoDate'][0:4]
        month = lotto['drwNoDate'][5:7]
        day = lotto['drwNoDate'][8:]

        return year, month, day


    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        draw_number = draw_number
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        lotto = json.load(lotto_json)
        main_numbers = [lotto['drwtNo1'], lotto['drwtNo2'], lotto['drwtNo3'], lotto['drwtNo4'], lotto['drwtNo5'], lotto['drwtNo6']]
        bonus_number = lotto['bnusNo']

        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        is_bonus = False

        for _ in range(len(line)):
            if line[_] in main_numbers:
                same_main_counts += 1

            if line[_] == bonus_number:
                is_bonus = True
                
        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        if same_main_counts == 6:
                ranking = 1
        elif same_main_counts == 5:
            if is_bonus == True:
                ranking = 2
            else:
                ranking = 3
        elif same_main_counts == 4:
            ranking = 4
        elif same_main_counts == 3:
            ranking = 5
        else:
            ranking = -1
            
        return ranking