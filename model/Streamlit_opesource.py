# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 13:52:07 2021

@author: NghiaNT
"""
import streamlit as st
#import numpy as np
import pandas as pd
import fasttext
from underthesea import word_tokenize
import regex as re



with st.sidebar.form(key ='Form1'):
    user_input = st.text_area("Nhập tiêu đề báo muốn tra:", "Hàng công đều ghi bàn giúp chủ nhà Liverpool thắng Arsenal 4-0 ở vòng 12 Ngoại hạng Anh tối 20/11.")
    Submit1 = st.form_submit_button(label = 'Lấy kết quả')

# Cache
@st.cache
def load_data1():
    df1 = pd.read_csv('500ksample_label_topic.csv', encoding="utf-8")
    return df1
label_topic = load_data1()

@st.cache
def load_data2():
    df2 = pd.read_csv('500ksample_label_sen.csv', encoding="utf-8")
    return df2
label_sen = load_data2()

@st.cache
def load_data3():
    df3 = pd.read_csv('stopwords.csv', encoding='utf-8')
    df4 = df3['stopwords'].tolist()
    return df4
list_stopwords = load_data3()

@st.cache(allow_output_mutation=True)
def load_model1():
    md1 = fasttext.load_model('model_topic.bin')
    return md1
model1 = load_model1()

@st.cache(allow_output_mutation=True)
def load_model2():
    md2 = fasttext.load_model('model_sen.bin')
    return md2
model2 = load_model2()

# Function

def text_preprocess(document):
    document = word_tokenize(document, format="text")
    document = document.lower()
    document = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]',' ',document)
    document = re.sub(r'\s+', ' ', document).strip()
    return document

def remove_stopwords(document):
    words = []
    for word in document.strip().split():
        if word not in list_stopwords:
            words.append(word)
    return ' '.join(words)

# Main

document = text_preprocess(user_input)
document = remove_stopwords(document)

pre_topic = model1.predict(document)
pre_sen = model2.predict(document)
result = pd.DataFrame({'topic_raw':[pre_topic[0][0]],
                       'topic_prob':[pre_topic[1][0]],
                       'sen_raw':[pre_sen[0][0]],
                       'sen_prob':[pre_sen[1][0]]})

result = result.merge(label_topic, on='topic_raw', how='left')
result = result.merge(label_sen, on='sen_raw', how='left')

st.title("Dataset-jsc AIV-group News Sentiment")
st.write('Mô tả dự án: Link đến tài liệu truyền thông của Dataset')
st.header('Kết quả dự đoán tiêu đề bài báo:')
st.header('Chủ đề: ')
st.write('Tiêu đề này thuộc chủ đề: ', result.loc[0,'topic_label'], ' với xác suất là: ', round(100*result.loc[0,'topic_prob'], 2), '%')
st.header('Sắc thái: ')
st.write('Tiêu đề này có sắc thái: ', result.loc[0,'sen_label'], ' với xác suất là: ', round(100*result.loc[0,'sen_prob'], 2), '%')














