# DANeS

## 1. Introduction

DANeS stands for "DATASET.VN and [AIV-Group](https://aivgroup.vn) News Sentiment". This is an open-source dataset that classifies topics and sentiment of e-newspaper's titles under the cooperation between  DATASET JSC (dataset.vn) and AIV Group (aivgroup.vn).

This document demontrates how to train model that can classify topics and sentiment of e-newspaper's titles by using Fasttext. FastText is an open-source library created by Facebook in 2016, it purpose is to support text classification and to train word embeded model

## 2. Setting:

You must install these packages:

* fasttext
* underthesea

## 3. Training model

### 3.1 Import necessary packages

```python
import pandas as pd
import numpy as np
import regex as re
import fasttext
from underthesea import word_tokenize
from sklearn.model_selection import train_test_split
```

### 3.2 Data Preprocessing for Model

*Split words (single word, compound word), convert words to lowercase, remove consecutive spaces

```python
def text_preprocess(document):
    document = word_tokenize(document, format="text")
    document = document.lower()
    document = re.sub(r'\s+', ' ', document).strip()
    return document
```

* Remove stopwords

```python
data = pd.read_csv('./stopwords.csv', encoding='utf-8')
list_stopwords = data['stopwords'].tolist()

def remove_stopwords(document):
    words = []
    for word in document.strip().split():
        if word not in list_stopwords:
            words.append(word)
    return ' '.join(words)
```

### 3.3 Input article titles

* Input data

```python
df = pd.read_csv('500ksample.csv', encoding="utf-8")
df.head()
```

title|publish_date|topic|sentiment
--------------|--------------|--------------|--------------
Vaccine COVID-19 dạng xịt mũi được thử nghiệm ...	| 2021-10-13 13:52:31+00:00| chinh_tri| 1
Mưa lũ làm 8 người thương vong và mất tích, gâ...	| 2021-10-17 23:16:28+00:00| moi_truong| 2


`title` is the article title

`publish_date` is time when the article was published

`topic` is the topic of the article: Politics, Environment, Life, News,...

`sentiment` is the title sentiment: 1: Positive, 2: Negative, 3: Neutral. 

* Process the data, convert it to a form suitable for fasttext packages

```python
df['sentiment'] = df['sentiment'].astype(str)
df.loc[:, 'sentiment'] = df.loc[:, 'sentiment'].apply(lambda x: '__label__' + x)
df.loc[:, 'topic'] = df.loc[:, 'topic'].apply(lambda x: '__label__' + x)
df = df[['title', 'topic', 'sentiment']]

df['title'] = df['title'].apply(text_preprocess)
df['title'] = df['title'].apply(remove_stopwords)
```

* Divide data to training and testing with the ratio 8/2 

```python
train, test = train_test_split(df, test_size = 0.2, random_state=42)
```

* Save train, test to use fasttext

```python
# Data topic model:
train[['topic', 'title']].to_csv('train1.txt', index = False, sep = ' ', header = None)
test[['topic', 'title']].to_csv('test1.txt', index = False,  sep = ' ', header = None)
# Data sentiment model:
train[['sentiment', 'title']].to_csv('train2.txt', index = False, sep = ' ', header = None)
test[['sentiment', 'title']].to_csv('test2.txt', index = False,  sep = ' ', header = None)
```

### 3.4 Train model, evaluate with test set, save model

* Topic

```python
# Training the fastText classifier topic
model1 = fasttext.train_supervised('train1.txt', dim=100, epoch=5, lr=0.1, wordNgrams=5, label='__label__')
# Evaluating performance on the entire test file
model1.test('test1.txt')   
model1.save_model('model1.bin')
```

* Sentiment

```python
# Training the fastText classifier sentiment
model2 = fasttext.train_supervised('train2.txt', dim=100, epoch=5, lr=0.1, wordNgrams=5, label='__label__')
# Evaluating performance on the entire test file
model2.test('test2.txt')   
model2.save_model('model2.bin')
```

### 3.5 Load model, predict new data

```python
model1 = fasttext.load_model('model1.bin')
model2 = fasttext.load_model('model2.bin')
document = "Trong không khí trang nghiêm, tiếng chuông chùa, nhà thờ ngân vang, người dân khắp cả nước cùng chắp tay cầu nguyện, thắp nến, thả hoa đăng tưởng niệm hơn 23.000 người mất vì Covid-19."

document = text_preprocess(document)
document = remove_stopwords(document)
pre_topic = model1.predict(document)
pre_sen = model2.predict(document)
result = pd.DataFrame({'topic_raw':[pre_topic[0][0]],
                      'topic_prob':[pre_topic[1][0]],
                      'sen_raw':[pre_sen[0][0]],
                      'sen_prob':[pre_sen[1][0]]
                      })
```

## Done!
