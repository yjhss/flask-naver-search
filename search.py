import os
import requests

from dotenv import load_dotenv
load_dotenv()

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")


def get_naver_search_results(query):

    client_id = NAVER_CLIENT_ID
    client_secret =NAVER_CLIENT_SECRET

    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    params = {"query": query}

    response = requests.get(url, headers=headers, params=params)
    return response.json(), response.status_code
  


# vercel 에서 실행할 때는 아래 코드를 주석처리해야 함    
# if __name__ == '__main__':
#     query = "성신여대"
#     results, code = get_naver_search_results(query)
#     print(code)
#     print(len(results['items']))
#     print(results['items'][0]['title'])

