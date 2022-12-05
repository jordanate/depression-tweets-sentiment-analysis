import streamlit as st
import pickle

from nltk.corpus import stopwords

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language="english")
stopwords_list = stopwords.words('english')


from nltk.tokenize import RegexpTokenizer
basic_token_pattern = r"(?u)\b\w\w+\b"
tokenizer = RegexpTokenizer(basic_token_pattern)

def stem_and_tokenize(document):
    tokens = tokenizer.tokenize(document)
    return [stemmer.stem(token) for token in tokens]


stemmed_stopwords = [stemmer.stem(word) for word in stopwords_list]

with open('model3a.pkl' , 'rb') as f:
    lr = pickle.load(f)

title = '<p style="font-weight:bold; color:Black; font-size:45px;">Depression in Tweets Detector</p>'

st.markdown(title, unsafe_allow_html=True)


prompt = '<p style="font-weight:bold; color:Black; font-size:20px;">Type a Tweet in the Box Below: </p>'

st.markdown(prompt, unsafe_allow_html=True)

n = st.text_input(' ')

n = [n]


sub_title = '<p style="font-weight:bold; color:Black; font-size:30px;">Possibility of Depression?</p>'

st.markdown(sub_title, unsafe_allow_html=True)

prediction = lr.predict(n)

no = '<p style="color:Black; font-size:20px;">No</p>'
yes = '<p style="color:Black; font-size:20px;">Yes</p>'

if prediction == [0]:
	st.markdown(no, unsafe_allow_html=True)

if prediction == [1]:
	st.markdown(yes, unsafe_allow_html=True)
