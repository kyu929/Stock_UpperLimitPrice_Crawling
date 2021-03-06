import requests
import os
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    "./chromedriver"
)

driver.implicitly_wait(3)

naver_finance_url = 'https://finance.naver.com/sise/'
naver_finance_market_url = 'https://finance.naver.com/sise/sise_market_sum.nhn?page=1'

driver.get(naver_finance_url)

stock_page_html = driver.page_source

soup = BeautifulSoup(stock_page_html, 'html.parser')
print(soup.select('#siselist_tab_0 > tbody'))
print(soup.find("div", attrs={"class": "box_type_l"}).find("table").find_all("a", attrs={"class": "tltle"}))

UpperLimitPrice_list = soup.find("div", attrs={"class": "box_type_l"}).find("table").find_all("a", attrs={"class": "tltle"})

for ULP in UpperLimitPrice_list:
    print(ULP.get_text().split())