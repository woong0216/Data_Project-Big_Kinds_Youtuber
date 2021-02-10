# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:12:57 2020

Big Kinds Period & Pytrend

@author: jaewoong Han
"""

import pandas as pd
data = pd.read_excel("./Big Kind 뉴스.xlsx")

# 불필요한 데이터 제거
del data['detail']
del data['Unnamed: 0']
del data['agency']

# 분기별 나누기
data['date']=data['date'].str.replace('-','')
data['date']=pd.to_numeric(data['date'])

# 2018-1분기
data_2018_1_1 = data['date'] >= 20180101
data_2018_1_2 = data['date'] <= 20180331
data_2018_1 = data[data_2018_1_1 & data_2018_1_2 ]

# 2018-2분기
data_2018_2_1 = data['date'] >= 20180401
data_2018_2_2 = data['date'] <= 20180631
data_2018_2 = data[data_2018_2_1 & data_2018_2_2 ]

# 2018-3분기
data_2018_3_1 = data['date'] >= 20180701
data_2018_3_2 = data['date'] <= 20180931
data_2018_3 = data[data_2018_3_1 & data_2018_3_2 ]

# 2018-4분기
data_2018_4_1 = data['date'] >= 20181001
data_2018_4_2 = data['date'] <= 20181231
data_2018_4 = data[data_2018_4_1 & data_2018_4_2 ]

# 2019-1분기
data_2019_1_1 = data['date'] >= 20190101
data_2019_1_2 = data['date'] <= 20190331
data_2019_1 = data[data_2019_1_1 & data_2019_1_2 ]

# 2019-2분기
data_2019_2_1 = data['date'] >= 20190401
data_2019_2_2 = data['date'] <= 20190631
data_2019_2 = data[data_2019_2_1 & data_2019_2_2 ]

# 2019-3분기
data_2019_3_1 = data['date'] >= 20190701
data_2019_3_2 = data['date'] <= 20190931
data_2019_3 = data[data_2019_3_1 & data_2019_3_2 ]

# 2019-4분기
data_2019_4_1 = data['date'] >= 20191001
data_2019_4_2 = data['date'] <= 20191231
data_2019_4 = data[data_2019_4_1 & data_2019_4_2 ]

# 2020-1분기
data_2020_1_1 = data['date'] >= 20200101
data_2020_1_2 = data['date'] <= 20200331
data_2020_1 = data[data_2020_1_1 & data_2020_1_2 ]

# 2020-2분기
data_2020_2_1 = data['date'] >= 20200401
data_2020_2_2 = data['date'] <= 20200631
data_2020_2 = data[data_2020_2_1 & data_2020_2_2 ]

# 분기별 사건 뉴스
col_names = ['2018-1','2018-2','2018-3','2018-4','2019-1','2019-2','2019-3','2019-4','2020-1','2020-2']

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# font_path = 'C:\\Windows\\Fonts\\NanumGothic.ttf'
font_path = 'C:\\Users\\goldlab\\Downloads\\NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=18)



names = col_names
values = [len(data_2018_1), len(data_2018_2), len(data_2018_3), len(data_2018_4), len(data_2019_1), 
         len(data_2019_2), len(data_2019_3), len(data_2019_4), len(data_2020_1), len(data_2020_2)]

plt.figure(figsize=(25, 5))

plt.subplot(131)
plt.bar(names, values)
plt.title('분기별 유튜버 관련 뉴스 건수',fontproperties=fontprop)
plt.show()

# 엑셀 저장
data_2018_1.to_excel('data_2018_1_.xlsx')
data_2018_2.to_excel('data_2018_2_.xlsx')
data_2018_3.to_excel('data_2018_3_.xlsx')
data_2018_4.to_excel('data_2018_4_.xlsx')
data_2019_1.to_excel('data_2019_1_.xlsx')
data_2019_2.to_excel('data_2019_2_.xlsx')
data_2019_3.to_excel('data_2019_3_.xlsx')
data_2019_4.to_excel('data_2019_4_.xlsx')
data_2020_1.to_excel('data_2020_1_.xlsx')
data_2020_2.to_excel('data_2020_2_.xlsx')

# pytrend를 통한 유튜버 검색 추이
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

# 검색 keyword, 검색 기간 입력
keyword1 = "youtuber"
period = "2005-01-01 2020-06-12"  #검색기간: 최근 5년

# Google Trend 접속 및 데이터 탑재
trend_obj = TrendReq()     # 검색 객체를 생성
trend_obj.build_payload(kw_list=[keyword1], timeframe=period)  #kw_list: 최대 5개
trend_df = trend_obj.interest_over_time()

# 그래프 출력
plt.style.use("ggplot")
plt.figure(figsize=(14,5))
trend_df[keyword1].plot()

plt.title((f'Google Trends: {keyword1}'), size=15)
plt.legend(loc="best")

# 그래프 파일 저장

plt.show()





























