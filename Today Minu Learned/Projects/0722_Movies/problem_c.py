import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  

    all_movie = [] # 전체 영화 정보 목록 리스트를 만들어줍니다.
    for c in range(len(movies)): # 전체 영화 갯수만큼 for문이 돌아갑니다.


        gen_name = [] # 이하 내용은 똑같습니다.(리스트 속 디렉토리이므로 디렉토리 경로만 수정했습니다.)
        for i in range(len(movies[c]['genre_ids'])):
            
            gen_num = movies[c]['genre_ids'][i]
            for x in range(len(genres)):
                if genres[x]['id'] == gen_num:
                    gen_name.append(genres[x]['name'])

        movie_data = {
            'id' : movies[c]['id'],
            'title' : movies[c]['title'],
            'poster_path' : movies[c]['poster_path'],
            'vote_average' : movies[c]['vote_average'],
            'overview' : movies[c]['overview'],
            'genre_ids' : gen_name
        }
        all_movie.append(movie_data)
    pprint(all_movie)
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
