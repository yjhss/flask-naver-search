import os
from dotenv import load_dotenv
load_dotenv()

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

from flask import Flask, render_template, request, jsonify
import requests

import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from search import get_naver_search_results

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results, code = get_naver_search_results(query)

    if code == 200:
        return render_template('results.html', query=query, results=results)
    else:
        return jsonify({"error": "Error Code:" + str(code)})


@app.route('/search_api', methods=['GET'])
def search_api():
    query = request.args.get('query')
    results, code = get_naver_search_results(query)

    if code == 200:
        return results
    else:
        return jsonify({"error": "Error Code:" + str(code)})



# vercel 에서 실행할 때는 아래 코드를 주석처리해야 함    
if __name__ == '__main__':
    app.run(debug=True)
