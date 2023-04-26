import csv
import requests
from bs4 import BeautifulSoup

# WebページのURLを指定
# Web페이지 URL를 지정
url = "https://smartstore.naver.com/unaidun"

# Webページを取得してHTMLを解析
# Web페이지를 수집하고 HTML를 분석
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# 商品タイトルとURL、価格、レーティング、画像URLを含む要素を抽出
# 상품title와 url, 가격, 후기(리뷰점수), 사진URL를 추출
data = []
titles = soup.select("#pc-wholeProductWidget > div > div > div > ul > li > div._2kRKWS_t1E strong._26YxgX-Nu5")
prices = soup.select("#pc-wholeProductWidget > div > div > div > ul > li > div._2kRKWS_t1E div._1zl6cBsmdy strong.zOuEHIx8DC span._2DywKu0J_8")
ratings = soup.select("#pc-wholeProductWidget > div > div > div > ul > li > div._2kRKWS_t1E div._1GFEfXrfT_ span._2fc0sZEHqG")
images = soup.select("#pc-wholeProductWidget > div > div > div > ul > li > div._2kRKWS_t1E img")

# データにカラム名を追加
# 데이터로 column명을 추가
data.append(["id", "title", "price(원)", "평점", "img", "url"])

# データをまとめる
# 데이터를 정리
for i in range(max(len(titles), len(prices), len(ratings), len(images))):
    title = titles[i].text.strip()
    price = prices[i].text.strip()
    rating = ratings[i].text.strip() if i < len(ratings) else "null"
    img = images[i]['src'] if i < len(images) else "null"
    data.append([i+1, title, price, rating, img, url])

# CSVファイルに書き込み
# CSV파일로 저장
with open("naver_store.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
print(f"{len(data)-1} records were written to the CSV file.")
