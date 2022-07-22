import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.
    gen_name = [] # 장르 이름을 텍스트로 출력할 리스트를 만듭니다.
    for i in range(len(movie['genre_ids'])): # 장르 번호를 gen_num변수에 할당하는 for문입니다.
        gen_num = movie['genre_ids'][i] # 장르 번호를 변수에 할당하여 아래 for문에 활용합니다.
        for x in range(len(genres)): # 제시된 장르 번호를 통해 장르 이름을 찾기 위한 for문입니다.
            if genres[x]['id'] == gen_num: # movie.json의 장르 번호와 genres.json의 장르 번호가 같은지 확인합니다.
                gen_name.append(genres[x]['name']) # 번호가 같다면 해당 장르 이름을 장르 리스트에 추가합니다.

    movie_data = {
        'id' : movie['id'],
        'title' : movie['title'],
        'poster_path' : movie['poster_path'],
        'vote_average' : movie['vote_average'],
        'overview' : movie['overview'],
        'genre_ids' : gen_name # 위에서 만들어진 리스트를 출력합니다.
    }

    return movie_data

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
