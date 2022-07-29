import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다. 
    
    URL_1 = f'https://api.themoviedb.org/3/search/movie?api_key=51790401a4babecb78bc0eca24db117c&language=ko-KR&query={title}&page=1&include_adult=false'

    response = requests.get(URL_1).json()
    if len(response["results"]) > 0:
        movie_id = response["results"][0]["id"]
    else:
        return None
        
    URL_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=51790401a4babecb78bc0eca24db117c&language=ko-KR'

    cast = []
    crew = []

    response_credits = requests.get(URL_2).json()
    for i in range(len(response_credits["cast"])):
        if response_credits["cast"][i]["order"] < 10:
            cast.append(response_credits["cast"][i]["name"])
        
        if response_credits["crew"][i]["department"] == "Directing":
            crew.append(response_credits["crew"][i]["name"])


    credits = {'cast' : cast, 'directing' : crew}

    return credits



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
