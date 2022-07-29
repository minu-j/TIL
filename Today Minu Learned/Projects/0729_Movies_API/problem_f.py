import requests
from pprint import pprint


def rank():
    pass 
    # 여기에 코드를 작성합니다. 

    print('================================')
    print('     박스오피스 순위 검색기     ')
    print('         (2003.11.11~)')
    print('================================')
    
    target_date = input('날짜 정보를 입력하세요(YYYYMMDD) : ')

    URL = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={target_date}'

    response = requests.get(URL).json()
    
    for i in range(len(response["boxOfficeResult"]["dailyBoxOfficeList"])):
        inten = 0
        if int(response["boxOfficeResult"]["dailyBoxOfficeList"][i]["rankInten"]) > 0:
            inten = '\033[32m' + f'▲{abs(int(response["boxOfficeResult"]["dailyBoxOfficeList"][i]["rankInten"]))}'
        elif int(response["boxOfficeResult"]["dailyBoxOfficeList"][i]["rankInten"]) < 0:
            inten = '\033[31m' + f'▼{abs(int(response["boxOfficeResult"]["dailyBoxOfficeList"][i]["rankInten"]))}'
        else:
            inten = '－'

        print(f'{inten}', '\033[37m' + f'#{response["boxOfficeResult"]["dailyBoxOfficeList"][i]["rank"]}위 {response["boxOfficeResult"]["dailyBoxOfficeList"][i]["movieNm"]} ({response["boxOfficeResult"]["dailyBoxOfficeList"][i]["audiCnt"]}명)')



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    rank()
