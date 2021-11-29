import pandas as pd
import numpy as np
import regex as re
import fasttext
from underthesea import word_tokenize
from sklearn.model_selection import train_test_split

# Preprocessing
def text_preprocess(document):
    document = word_tokenize(document, format="text")
    document = document.lower()
    document = re.sub(r'\s+', ' ', document).strip()
    return document

data = pd.read_csv('./stopwords.csv', encoding='utf-8')
list_stopwords = data['stopwords'].tolist()

def remove_stopwords(document):
    words = []
    for word in document.strip().split():
        if word not in list_stopwords:
            words.append(word)
    return ' '.join(words)


df = pd.read_csv('500ksample.csv', encoding="utf-8")
df['sentiment'] = df['sentiment'].astype(str)
df.loc[:, 'sentiment'] = df.loc[:, 'sentiment'].apply(lambda x: '__label__' + x)
df.loc[:, 'topic'] = df.loc[:, 'topic'].apply(lambda x: '__label__' + x)
df = df[['title', 'topic', 'sentiment']]

df['title'] = df['title'].apply(text_preprocess)
df['title'] = df['title'].apply(remove_stopwords)

train, test = train_test_split(df, test_size = 0.2, random_state=42)

# Data topic model:
train[['topic', 'title']].to_csv('train1.txt', index = False, sep = ' ', header = None)
test[['topic', 'title']].to_csv('test1.txt', index = False,  sep = ' ', header = None)
# Data sentiment model:
train[['sentiment', 'title']].to_csv('train2.txt', index = False, sep = ' ', header = None)
test[['sentiment', 'title']].to_csv('test2.txt', index = False,  sep = ' ', header = None)

# Training the fastText classifier topic
model1 = fasttext.train_supervised('train1.txt', dim=100, epoch=5, lr=0.1, wordNgrams=5, label='__label__')
# Evaluating performance on the entire test file
model1.test('test1.txt')   
model1.save_model('model1.bin')

# Training the fastText classifier sentiment
model2 = fasttext.train_supervised('train2.txt', dim=100, epoch=5, lr=0.1, wordNgrams=5, label='__label__')
# Evaluating performance on the entire test file
model2.test('test2.txt')   
model2.save_model('model2.bin')

# File label + sentiment
label_topic = pd.DataFrame(df['topic'].unique(), columns = ['topic_raw']) 
label_topic['topic_label'] = ['Chính trị', 'Môi trường','Đời sống','Thời sự','Công nghệ','Thể thao','Nhà đất','Pháp luật','Giáo dục','Khoa học','Thế giới','Giao thông','Xã hội','Giải trí','Kinh tế','Văn hóa']

label_sen = pd.DataFrame(df['sentiment'].unique(), columns = ['sen_raw']) 
label_sen['sen_label'] = ['Tích cực','Tiêu cực','Trung tính','Chưa xác định']



