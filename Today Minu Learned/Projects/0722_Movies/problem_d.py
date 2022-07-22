import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    revenue = 0 # 영화 수익 값을 저장할 변수를 만듭니다.
    for i in range(len(movies)): # 영화의 갯수만큼 반복합니다.
        id = movies[i]['id'] # 영화 목록에서 id를 불러옵니다.
        movie_json = open(f'data/movies/{id}.json', encoding='utf-8') # 부러온 id에 해당하는 파일 이름을 f-string으로 지정하고, 해당 파일을 불러옵니다.
        movie = json.load(movie_json) # 해당 파일의 정보를 디렉토리에 할당합니다.

        if movie['revenue'] > revenue: # 만약 해당 영화의 수익이 변수값의 수익보다 크다면
            revenue = movie['revenue'] # 수익 변수에 해당 영화의 수익를 할당하고
            title = movie["title"] # 타이틀 변수에 해당 영화의 제목을 할당합니다.
        else:
            continue
    print(title) # 저장된 영화의 타이틀을 불러옵니다.

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
