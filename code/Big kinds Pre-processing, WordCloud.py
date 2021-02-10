# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:28:40 2020

Big Kinds Pre-processing, WordCloud

@author: jaewoong Han
"""

# keyword Analysis (Pre-processing) 2018년 1분기 예시
import pandas as pd
data_2018_1 = pd.read_excel("./data_2018_1_.xlsx")
stop_words =['유튜버','유튜브','사람','주장','대해','관련','기자','지난','방송','수사','얘기', '앵커', '문제','최신','통해','위해','정도'
            ,'동물','대표','제기','사진','요구','아이','진행',' 대한','내용','지금','이유','확인','사용','사실','생각','부분', '때문',
            '대한','우리','이후','이번', '당시','라며','다른','지난해', '모두','해당','이법','표현','과정']
# general한 단어 및 뉴스 관련 단어 제거 korean stopwords에 명시된 단어들 중 명사로 요구될 수 있는 단어들만 추출

def flat_list(array): 
    a=[]
    for i in array:
        if type(i) == type(list()):
            a+=(flat_list(i))       
        else:
            a.append(i)
    return a

# pre-processing
content=[]
for w in data_2018_1['content']:
    a = w.replace('\n','')
    content.append(a)
content1 = str(content)

# pos-tagging
from konlpy.tag import Twitter
 
twitter = Twitter()
tagged_list = twitter.pos(content1)
print(twitter.pos(content1))

# noun extracting
goyou = []
for t in tagged_list:
    if (t[1] == 'Noun') and len(str(t[0])) >=2 :
        goyou.append(t[0])
goyou = [each_word for each_word in goyou if each_word not in stop_words]
from collections import Counter
abstract_list = flat_list(goyou)
abstract = Counter(abstract_list)

import nltk
from pprint import pprint
text = nltk.Text(goyou, name='NMSC')

# 전체 토큰의 개수
print(len(text.tokens))

# 중복을 제외한 토큰의 개수
print(len(set(text.tokens)))            

# 출현 빈도가 높은 상위 토큰 10개
pprint(text.vocab().most_common(10))

# 내림순위
from collections import OrderedDict
def sort_by_key(t):
    return t[1]
for k, v in OrderedDict(sorted(abstract.items(), key=sort_by_key, reverse=True)).items():
    print(k, v)
    
    
    
# WordCloud
import nltk
ko = nltk.Text(goyou, name='유튜버')
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

data = ko.vocab().most_common(150)
wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf', relative_scaling = 0.2, background_color = 'white').generate_from_frequencies(dict(data))
plt.figure(figsize=(12,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()