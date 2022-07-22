import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.
    title = [] # 제목을 저장할 리스트를 만듭니다.
    for i in range(len(movies)):
        id = movies[i]['id']
        movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movie = json.load(movie_json) # D와 동일

        release_date = list(movie['release_date']) # 개봉일을 리스트로 가져옵니다.

        # 텍스트 사이에 있는 특정 글자들의 정보(몇월인지)를 알기 위해 텍스트를 리스트로 분해했는데,
        # 더 좋은 방법이 있을 것 같습니다.

        release_date = release_date[5:7] # 5, 6번째 값을 가져옵니다.(몇월인지)

        if release_date == ['1', '2']: # 만약 가져온 월이 12월이라면
            title.append(movie["title"]) # 제목을 제목 리스트에 추가합니다.
        else:
            continue
    return title

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))