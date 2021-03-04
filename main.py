import requests
import os
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    'C:/Users/User/Documents/Git/Stock_UpperLimitPrice_Crawling/chromedriver.exe'
)

driver.implicitly_wait(3)

driver.get('https://finance.naver.com/sise/')

stock_page_html = driver.page_source
soup = BeautifulSoup(stock_page_html, 'html.parser')

print(soup.select('#siselist_tab_0 > tbody > tr:nth-child(3) > td:nth-child(4)'))
