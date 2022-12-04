import streamlit as st
import pickle


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

n = st.number_input('Type a tweet', step=1)

st.write('Possibility of Depression?')

st.write(f'{n}')