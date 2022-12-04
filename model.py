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

with open('model3.pkl' , 'rb') as f:
    lr = pickle.load(f)

st.title('Depression in Tweets Detector')

n = st.text_input('Type a tweet')

n = [n]

st.write('Possibility of Depression?')

prediction = lr.predict(n)

if prediction == [0]:
	st.write('No')
if prediction == [1]:
	st.write('Yes')