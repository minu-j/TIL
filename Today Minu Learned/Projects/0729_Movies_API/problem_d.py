import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다. 

    URL_1 = f'https://api.themoviedb.org/3/search/movie?api_key=51790401a4babecb78bc0eca24db117c&language=ko-KR&query={title}&page=1&include_adult=false'

    movie_id = ''

    response = requests.get(URL_1).json()
    if len(response["results"]) > 0:
        movie_id = response["results"][0]["id"]
    else:
        return None

    URL_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=51790401a4babecb78bc0eca24db117c&language=ko-KR&page=1'

    recommend_movie = requests.get(URL_2).json()
    recommends = []
    if recommend_movie['results'] == []:
        return []

    else:
        for i in range(len(recommend_movie['results'])):
            recommends.append(recommend_movie['results'][i]["title"])

    return recommends

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
