import requests
from bs4 import BeautifulSoup

stock_page = requests.get("https://finance.naver.com/sise/")
stock_page_html = stock_page.text

soup = BeautifulSoup(stock_page_html, 'html.parser')
print(soup.find_all(attrs={'summary': '탑종목 상한가 리스트'}))
