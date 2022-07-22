import json
from pprint import pprint


def movie_genre(movies, genre):
    pass 
    # 여기에 코드를 작성합니다.

    print('*******************************************')
    print('**      장 르 별   영 화   추 천 기      **')
    print('*******************************************')
    print('')
    for x in range(len(genre)):
        print(f'{x+1}.', genre[x]['name'])
        

    genre_num = int(input('\n > 보고싶은 장르의 번호를 입력하세요 : '))

    genre_num = genre[genre_num-1]['id']

    title = [] # 제목을 저장할 리스트를 만듭니다.

    for y in range(len(movies)):
        for z in range(len(movies[y]['genre_ids'])):
            if movies[y]['genre_ids'][z] == genre_num:
                title.append(movies[y]['title'])
        else:
            continue
    print('\n > 제가 추천드리는 영화는!')
    return title

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_genre(movies_list, genres_list))