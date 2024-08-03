import os
from dotenv import load_dotenv
load_dotenv()

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

from flask import Flask, render_template, request
import requests

from search import get_naver_search_results

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = get_naver_search_results(query)
    return render_template('results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
