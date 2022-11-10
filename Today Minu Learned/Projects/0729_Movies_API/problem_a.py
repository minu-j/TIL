import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  

    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page=1'

    response = requests.get(URL).json()
    return len(response["results"])

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
