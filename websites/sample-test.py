import requests

# WebページのURLを指定
# 가져 오고 싶은 Web페이지 URL를 지정
url = ""

# Webページを取得してHTMLを解析
# Web페이지를 수집하고 HTML를 분석
response = requests.get(url)

# 200が返ってくるか確認
# 기대치 200가 오면 된다. 사용하기 쉬운 사이트(403가 오면 힘들어)
print(response)