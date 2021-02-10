# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 20:28:40 2020

Big Kinds TF-IDF, Embedding, LDA

@author: Jaewoong Han
"""

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pandas as pd
data = pd.read_excel("./data_2018_1_.xlsx") # 예시

# noun extracting
list_tf=[]

for a in data['content']:
    a=str(a)
    tagged_list = twitter.pos(a)
    gain=[]
    for t in tagged_list:
        if (t[1] == 'Noun') and len(str(t[0])) >=2 and (str(t[0]!='유튜브')) and (str(t[0]!='유튜버')):
            gain.append(t[0])
    list_tf.append(gain)
data['keyword']=list_tf

# 소문자 및 stopwords 및 부호 제거 및 stemming
tf_idf=[]
tf_idf_contents = []
list_a = ['유튜버','유튜브','사람','주장','대해','관련','기자','지난','방송','수사','얘기', '앵커', '문제','최신','통해','위해','정도'
            ,'동물','대표','제기','사진','요구','아이','진행',' 대한','내용','지금','이유','확인','사용','사실','생각','부분', '때문',
            '대한','우리','이후','이번', '당시','라며','다른','지난해', '모두','해당','이법','표현','과정']
stop_list = set(list_a)

for abstract in data['keyword']:
    abstract=str(abstract)
    abstract = abstract.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokenize_list = tokenizer.tokenize(abstract)
    
    result = []
    for w in tokenize_list:
        if w not in stop_list:
            result.append(w)
    
    tf_idfs = " ".join(result)
    tf_idf_contents.append(tf_idfs)    
    
# CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
vect.fit(tf_idf_contents)
vect.vocabulary_

# bi-gram 확인
vect = CountVectorizer(ngram_range=(2, 2)).fit(tf_idf_contents)
vect.vocabulary_

import pandas as pd
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from future.utils import iteritems
from collections import Counter
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

as_one = ''
for document in tf_idf_contents:
    as_one = as_one + ' ' + document
words = as_one.split()
counts = Counter(words) # 숫자 확인
vocab = sorted(counts, key=counts.get, reverse=True) # 분류
word2idx = {word.encode("utf8").decode("utf8"): ii for ii, word in enumerate(vocab,1)}
idx2word = {ii: word for ii, word in enumerate(vocab)}

V = len(word2idx)
N = len(tf_idf_contents)

tf = CountVectorizer()
tf.fit_transform(tf_idf_contents)
tf.fit_transform(tf_idf_contents)[0:1].toarray()

# 30차원으로 임베딩
tfidf = TfidfVectorizer(max_features = 30, max_df=0.95, min_df=0)
A_tfidf_sp = tfidf.fit_transform(tf_idf_contents)
tfidf_dict = tfidf.get_feature_names()
data_array = A_tfidf_sp.toarray()
data = pd.DataFrame(data_array, columns=tfidf_dict)
tsne = TSNE(n_components=2, n_iter=10000, verbose=1)
Z = tsne.fit_transform(data_array.T)

# 2차원으로 시각화
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# font_path = 'C:\\Windows\\Fonts\\NanumGothic.ttf'
# font_path = 'C:\\Users\\goldlab\\Downloads\\NanumGothic.ttf'
path = 'C:\\Users\\goldlab\\Downloads\\NanumGothic.ttf'
fontprop = fm.FontProperties(fname=path, size=10)
plt.scatter(Z[:,0], Z[:,1])
for i in range(len(tfidf_dict)):
    plt.annotate(s=tfidf_dict[i].encode("utf8").decode("utf8"), xy=(Z[i,0], Z[i,1]),fontProperties =fontprop)

plt.draw()




# LDA
import random
from collections import Counter

K=4
documents=list_tf

# a list of Counters, one for each document
document_topic_counts = [Counter() for _ in documents]

# a list of Counters, one for each topic
topic_word_counts = [Counter() for _ in range(K)]

# a list of numbers, one for each topic
topic_counts = [0 for _ in range(K)]

document_lengths = list(map(len, documents))
document_lengths # 기사 당 단어 수 (중복 제거)

distinct_words = set(word for document in documents for word in document)
W = len(distinct_words)
W # 단어의 수

D = len(documents)
D # 기사의 수

def topic_weight(d, word, topic):

    def p_topic_given_document(topic, d, alpha=0.1):
        
        return ((document_topic_counts[d][topic] + alpha) / (document_lengths[d] + K * alpha))

    def p_word_given_topic(word, topic, beta=0.1):
        
        return ((topic_word_counts[topic][word] + beta) / (topic_counts[topic] + W * beta))
    
    
    return p_word_given_topic(word, topic) * p_topic_given_document(topic, d)

def choose_new_topic(d, word):
    
    def sample_from(weights):
        total = sum(weights)
        rnd = total * random.random()
        for i, p in enumerate(weights):
            rnd -= p
            if rnd <= 0: 
                return i
        
    return sample_from([topic_weight(d, word, topic) for topic in range(K)])

document_topics = [[random.randrange(K) for word in document] for document in documents]

for d in range(D):
    for word, topic in zip(documents[d], document_topics[d]):
        document_topic_counts[d][topic] += 1 
        topic_word_counts[topic][word] += 1
        topic_counts[topic] += 1
        
for epoch in range(100): # repetition
    for d in range(D): # each documnet
        for i, (word, topic) in enumerate(zip(documents[d],document_topics[d])):
            
            document_topic_counts[d][topic] -= 1 # 문서별 토픽 갯수
            topic_word_counts[topic][word] -= 1 # 토픽별 단어 갯수
            topic_counts[topic] -= 1 # 토픽별 카운트
            document_lengths[d] -= 1 # 문서별 단어갯수
        
            new_topic = choose_new_topic(d, word)
            document_topics[d][i] = new_topic
            
            document_topic_counts[d][new_topic] += 1 # 문서별 토픽 갯수
            topic_word_counts[new_topic][word] += 1 # 토픽별 단어 갯수
            topic_counts[new_topic] += 1 # 토픽별 카운트
            document_lengths[d] += 1 # 문서별 단어갯수
            
df = pd.DataFrame(columns=['Topic1','Topic2','Topic3','Topic4'], index=['Top'+str(i) for i in range(1,6)])

for k, word_counts in enumerate(topic_word_counts):
    for ix, (word, count) in enumerate(word_counts.most_common(5)): # 각 토픽별로 top 5단어
            df.loc['Top'+str(ix+1),'Topic'+str(k+1)] = word+'({})'.format(count)
            
df_dict = pd.DataFrame(df)
df_dict # 토픽에 따른 word 추

























    