# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:03:32 2020


Big Kinds Crawling

@author: jaewoong han
"""

import pandas as pd
import requests
from selenium import webdriver
import time
import random
from tqdm import tqdm
import request
from bs4 import BeautifulSoup
driver = webdriver.Chrome('./chromedriver.exe')  
#C:\\Users\\User\\Desktop\\다운로드\\chromedriver.exe
#C:\\Users\\goldlab\\Downloads\\chromedriver.exe'


url="https://www.bigkinds.or.kr/v2/news/index.do"
driver.get(url)

keywords = '유튜버'
driver.find_element_by_id('total-search-key').send_keys(keywords)
driver.implicitly_wait(2)

# 기간 누르기
driver.find_element_by_css_selector('#date-filter-btn').click()
driver.implicitly_wait(2)

# 전체 누르기
driver.find_element_by_css_selector('#date-filter-div > div > div:nth-child(1) > button.btn.btn-sm.w-100.main-search-filters__dropdown__btn.date-select-btn').click()
driver.implicitly_wait(2)

# 적용 누르기
driver.find_element_by_css_selector('#date-confirm-btn').click()

# 통합 누르기
driver.find_element_by_css_selector('#category-filter-btn').click()

# 사회
driver.find_element_by_css_selector('#category-tree-wrap > ul > li:nth-child(3)').click()

# 적용 누르기
driver.find_element_by_css_selector('#collapse-step-1 > div > div > div > div > div.main-search-filters.text-left.mt-2 > div.dropdown.main-search-filters__item.open > div > div.action-wrap > button.btn.btn-sm.btn-primary.close-filter-btn').click()

# 사건사고 누르기
driver.find_element_by_css_selector('#incident-filter-btn').click()

# 범죄 사고
driver.find_element_by_css_selector('#incident-tree-wrap > ul > li:nth-child(1) > div').click()
driver.find_element_by_css_selector('#incident-tree-wrap > ul > li:nth-child(2) > div').click()

# 적용 누르기
driver.find_element_by_css_selector('#collapse-step-1 > div > div > div > div > div.main-search-filters.text-left.mt-2 > div.dropdown.main-search-filters__item.open > div > div.action-wrap > button.btn.btn-sm.btn-primary.close-filter-btn').click()

# 검색어 버튼 누르기
driver.find_element_by_css_selector('#collapse-step-1 > div > div > div > div > div.input-group.main-search__form > span > button').click()

# 제목, 내용, 분류, 일자, 기관
title = []
content = []
detail = []
date = []
agency = []

# for k in tqdm(range(1, 30)):   # 큰창 돌리기
# for j in tqdm(range(1, 9)):   # 다음 칸 돌리기
#     if j==1:
#         pass


#     else :
#         driver.find_element_by_css_selector('#news-results-pagination > ul > li:nth-child('+ str(j+2)+') > a').click() # 안먹힐경우에는 다음칸 누르기
#         time.sleep(10)

for i in tqdm(range(1,  101)) : # 100건씩 추출

    driver.find_element_by_xpath('//*[@id="news-results"]/div['+ str(i) +']/div[2]/h4').click()
    b= driver

    # 본문 끌어오기
    html = b.page_source
    bs_obj = BeautifulSoup(html,'html.parser')
    time.sleep(2)

    # 제목 추출
    title_news = bs_obj.findAll('h4',{'id':'myModalLabel'})
    aaa = title_news[1].text.strip()
    title.append(aaa)

    # 내용추출
    content_news = bs_obj.find('div',{'class':'news-detail__content'})
    content.append(content_news.text.strip())

    # 분류
    detail_news = bs_obj.find('span', {'class' : 'news-detail__header-item hidden'})
    detail.append(detail_news.text.strip())

    # 일자
    date_news = bs_obj.findAll('span', {'class' : 'news-detail__header-item'})
    bbb = date_news[3].text.strip()
    date.append(bbb)

    # 기관
    img = bs_obj.findAll('img',{'height' : 30})
    agency.append(img[0].get('src'))


    driver.find_element_by_xpath('//*[@id="news-detail-modal"]/div/div/div[3]/button').click()
    
    
# 리스트 판다스 형태
dict = {'title':title, 'detail':detail, 'date':date, 'agency':agency, 'content':content}
df_dict = pd.DataFrame(dict)

# 엑셀 저장
df_dict.to_excel('Big Kind2.xlsx')















