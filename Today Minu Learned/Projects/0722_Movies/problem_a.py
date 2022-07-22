import json
from pprint import pprint


def movie_info(movie):
    
    # 여기에 코드를 작성합니다.    
    movie_data = { # 필요한 영화 정보만 추출해서 새로운 디렉토리를 생성합니다.
        'id' : movie_dict['id'],
        'title' : movie_dict['title'],
        'poster_path' : movie_dict['poster_path'],
        'vote_average' : movie_dict['vote_average'],
        'overview' : movie_dict['overview'],
        'genre_ids' : movie_dict['genre_ids']
    }
    return movie_data # 영화 정보 디렉토리를 리턴합니다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
