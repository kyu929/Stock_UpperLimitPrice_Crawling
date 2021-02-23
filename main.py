import requests

stock_page = requests.get("https://finance.naver.com/sise/")
print(stock_page.text)
