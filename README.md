# Using Text Mining to Analyze Social Issues Related to 'YouTuber'

## Background
- Youtube was born in February 2005. 
- As of June 01, 2020, the most popular YouTuber has over 100 million subscribers. 
- As there are more YouTubers, there are many social controversies.
- The trend of Youtuber spreading on Google.

> Using Pytrend <br/>

![trend](https://user-images.githubusercontent.com/63955072/122730588-5ca28380-d2b5-11eb-9c84-100d3bf1c352.png)

## Propose
- There was a lot of understanding of YouTube's trends, but there was a lack of connection with social issues.
> There were many simple trends without mentioning the problems of YouTube. <br/>
> There were many studies that improved content capabilities by identifying customer tendencies through YouTube comments. <br/>
> There is little research on how influential YouTubers are in social issues and where they stand out. <br/>
> Data research on shortcomings is weak, so we want to extract social issues by analyzing news articles, which are objective press releases. <br/>

## Dataset
- Data Source: Big KINDS

![bigkinds](https://user-images.githubusercontent.com/63955072/122730974-c91d8280-d2b5-11eb-85b8-d9006518cdc9.png)

- Data Crawling

![Data Crawling](https://user-images.githubusercontent.com/63955072/122731319-1f8ac100-d2b6-11eb-8722-c7b1cd178f24.png)

## Method
- Process by Data Quarter

![Data Quarter](https://user-images.githubusercontent.com/63955072/122731574-6678b680-d2b6-11eb-9225-afebb1575bb9.png)

- Data Preprocessing
> Noun Extracting <br/>

![Data Preprocessing](https://user-images.githubusercontent.com/63955072/122731755-91fba100-d2b6-11eb-8177-780532c3c047.png)

## Analysis
- WordCloud
> It generated issues every quarter. <br/>

> 2018-1 WordCloud (example) <br/>

![2018-1 wordcloud](https://user-images.githubusercontent.com/63955072/122732298-1e0dc880-d2b7-11eb-86db-06b37fb18689.png)

> 2018-2 WordCloud (example) <br/>

![2018-2 wordcloud](https://user-images.githubusercontent.com/63955072/122732446-3ed61e00-d2b7-11eb-878c-757a5923f28e.png)

- TF-IDF
> Visualization using t-NSE <br/>
> Embedding <br/>

> 2018-1 t-NSE (example) <br/>

![TF-IDF 1](https://user-images.githubusercontent.com/63955072/122732856-a0968800-d2b7-11eb-8c47-95bd25e2a470.png)

> 2018-2 t-NSE (example) <br/>

![TF-IDF 2](https://user-images.githubusercontent.com/63955072/122732926-abe9b380-d2b7-11eb-9856-ba318bdaf855.png)

- LDA
> LDA Topic Modeling <br/>

> 2018-1 LDA Topic Modeling (example) <br/>

![Topic 1](https://user-images.githubusercontent.com/63955072/122733368-13076800-d2b8-11eb-8d13-4f55d0ee2573.png)

> 2018-2 LDA Topic Modeling (example) <br/>

![Topic 2](https://user-images.githubusercontent.com/63955072/122733467-29adbf00-d2b8-11eb-85e5-6f422aa3e5ee.png)

## Conclusion
- Among social issues, the scope of YouTubers was the most mentioned political and gender issues.
- We have come to reflect on the problems that arise in the society of YouTubers mentioned in the news.
- Major events could be identified.
> Yang Ye-won case, Youtuber threatening Yoon Seok-yeol, YouTuber posing as a Corona patient, and a number of assaults by YouTubers (dogs, girlfriends, alumni) <br/>
- With the creation of YouTubers, assault-related incidents were the most common among social problems.
- LDA makes it easier to get a topical grip on the events.
- There is a point that social problems of YouTubers and social problems mentioned by YouTubers are not separated because they are derived together.
- When dealing with network analysis, it is judged that the relationship between each document can be verified.


