import json
from pprint import pprint
import random
from tkinter import Y


def movie_quiz(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.


    print('******************************************')
    print('**            영  화  퀴  즈            **')
    print('******************************************')
    print('')

    retry = 'y'
    while retry == 'y':
        answer_num = random.randint(0, 22) # 랜덤으로 숫자를 불러옵니다.(영화 갯수인 22만큼)
        id = movies[answer_num]['id'] # 불러온 숫자로 영화 id번호를 가져옵니다.

        # print(id)

        movie_json = open(f'data/movies/{id}.json', encoding='utf-8') # id에 해당하는 파일 이름을 f-string으로 지정하고, 해당 파일을 불러옵니다.
        movie = json.load(movie_json) # 해당 파일의 정보를 디렉토리에 할당합니다.

        answer = movie['title'] # 제목을 정답으로 할당합니다.

        runtime_h = movie['runtime'] // 60 # 상영시간을 시간, 분으로 바꿉니다.
        runtime_m = movie['runtime'] % 60

        production = [] # 제작사를 가져오고, 리스트에 저장합니다.
        for i_p in range(len(movie['production_companies'])): # 제작사 리스트의 길이만큼 반복하여 리스트에 추가합니다.
            production.append(movie['production_companies'][i_p]['name'])

        genre = [] # 장르 이름을 텍스트로 출력할 리스트를 만듭니다.
        for x_g in range(len(movie['genres'])): # 장르 번호를 gen_num변수에 할당하는 for문입니다.
            gen_num = movie['genres'][x_g]['id'] # 장르 번호를 변수에 할당하여 아래 for문에 활용합니다.
            for y_g in range(len(genres)): # 제시된 장르 번호를 통해 장르 이름을 찾기 위한 for문입니다.
                if genres[y_g]['id'] == gen_num: # movie.json의 장르 번호와 genres.json의 장르 번호가 같은지 확인합니다.
                    genre.append(genres[y_g]['name']) # 번호가 같다면 해당 장르 이름을 장르 리스트에 추가합니다.
                else:
                    continue

        release_date = movie['release_date'] # 개봉일을 변수에 할당합니다.



        title = list(movie['title']) # 영화 제목 리스트로 변환하여
        title_len = len(title) # 제목의 길이를 변수에 할당합니다.(띄어쓰기를 어떻게 지울지 모르겠습니다ㅠㅠ)

        overview = movie['overview'] # 줄거리를 변수에 할당합니다.

        '''
        변수 할당이 끝나면 퀴즈를 시작합니다.
        정답을 맞추면 break하고, 틀리면 게임을 계속 진행하는데,
        원래는 맞추거나 틀렸을 때, 실행되는 함수를 만들고 싶었는데,
        일단 어떻게 만들지 감이 안와서 if문 안에 if문을 무한으로 반복해놨습니다.
        '''


        print('힌트를 잘 보시고, 영화의 제목을 맞춰주세요.\n')
        print(f'이 영화의 상영시간은 {runtime_h}시간 {runtime_m}분입니다.')
        answer_title = input('입력하세요 : ')
        if answer_title == answer:
            print('정답입니다!')
            break
        else:
            print(f'땡! 오답입니다.\n힌트를 하나 더 드리겠습니다.\n\n이 영화의 제작사는 {production}입니다.')
            answer_title = input('입력하세요 : ')
            if answer_title == answer:
                print('정답입니다!')
                break
            else:
                print(f'땡! 오답입니다.\n힌트를 하나 더 드리겠습니다.\n\n이 영화의 장르는 {genre}입니다.')
                answer_title = input('입력하세요 : ')
                if answer_title == answer:
                    print('정답입니다!')
                    break
                else:                    
                    print(f'땡! 오답입니다.\n힌트를 하나 더 드리겠습니다.\n\n이 영화의 개봉일은 {release_date}입니다.')
                    answer_title = input('입력하세요 : ')
                    if answer_title == answer:
                        print('정답입니다!')
                        break
                    else:  
                        print(f'땡! 오답입니다.\n힌트를 하나 더 드리겠습니다.\n\n이 영화의 제목은 {title_len}글자입니다.(띄어쓰기 포함)')
                        answer_title = input('입력하세요 : ')
                        if answer_title == answer:
                            print('정답입니다!')
                            break
                        else:  
                            print(f'땡! 오답입니다.\n***************\n \n 마지막 힌트입니다...\n \n ***************\n영화의 줄거리를 알려드리겠습니다.\n{overview}')
                            answer_title = input('입력하세요 : ')
                            if answer_title == answer:
                                print('정답입니다!')
                                break
                            else:  
                                print(f'아쉽게 맞추지 못했습니다! 더 공부하세요\n정답은 {answer}입니다.')
                                retry = input('게임을 다시 하시겠습니까?(y/n) :' ) # 마지막까지 정답을 맞추지 못하면 게임을 다시 실행할지 여부를 물어봅니다.
                                if retry == 'y':
                                    continue
                                elif retry == 'n':
                                    break
    return 'end'

                



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_quiz(movies_list, genres_list))
