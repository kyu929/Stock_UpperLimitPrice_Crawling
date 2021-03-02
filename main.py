import requests
from bs4 import BeautifulSoup

stock_page = requests.get("https://finance.naver.com/sise/")
stock_page_html = stock_page.text

soup = BeautifulSoup(stock_page_html, 'html.parser')
print(soup.select('td > a'))
