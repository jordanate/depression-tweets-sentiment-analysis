import streamlit as st
import pickle
from PIL import Image

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

twitterlogo = Image.open('images/twitter_logo.png')

st.image(twitterlogo, width=100)

title = '<p style="font-weight:bold; color:Black; font-size:45px;">Depression in Tweets Detector</p>'

st.markdown(title, unsafe_allow_html=True)


prompt = '<p style="font-weight:bold; color:Black; font-size:22px;">Type a Tweet in the Box Below: </p>'

st.markdown(prompt, unsafe_allow_html=True) 

n = st.text_input(' ', max_chars=280)


button = st.button('Enter')

disclaimer_p1= '<p style="color:Black; font-size:15px;"><em>Disclaimer: This is not a diagnostic tool.</em></p>'
disclaimer_p2= '<p style="color:Black; font-size:15px;"><em>If you, or someone you know, is experiencing symptoms of depression, please refer to the resources listed below.</em></p>' 

st.markdown(disclaimer_p1, unsafe_allow_html=True)
st.markdown(disclaimer_p2, unsafe_allow_html=True)


if button: 
	sub_title = '<p style="font-weight:bold; color:Black; font-size:30px;">Indication of Depression?</p>'

	st.markdown(sub_title, unsafe_allow_html=True)

	n = [n]
	prediction = lr.predict(n)

	no = '<p style="color:Black; font-size:25px;">No</p>'
	yes = '<p style="color:Black; font-size:25px;">Yes</p>'

	if prediction == [0]:
		st.markdown(no, unsafe_allow_html=True)
	else:
		st.markdown(yes, unsafe_allow_html=True)

st.markdown("***")

resources_title = '<p style="font-weight:bold; color:Black; font-size:27px;">Mental Health Resources</p>'

st.markdown(resources_title, unsafe_allow_html=True)

cl = '<p style="color:Black; font-size:20px;"><strong>United States Suicide and Crisis Lifeline (24/7):</strong> Call 988 (No data charges)</p>'

nami = '<p style="color:Black; font-size:20px;"><strong>NAMI HelpLine (M-F, 10am - 10pm, ET):</strong> Call 1-800-950-NAMI (6264), Text "HelpLine" to 62640, or Email at <a href="mailto:helpline@nami.org"> helpline@nami.org </a> </p>'

samhsa = '<p style="color:Black; font-size:20px;"><strong>SAMHSA’s (Substance Abuse and Mental Health Services Administration) National Helpline (24/7):</strong> Call 1-800-662-HELP (4357)</p>'

textline = '<p style="color:Black; font-size:20px;"><strong>Crisis Text Line (24/7):</strong> Text HOME to 741741</p>'

betterhelp = '<p style="color:Black; font-size:20px;"><strong>BetterHelp Teletherapy:</strong> <a href="https://www.betterhelp.com/"> https://www.betterhelp.com/ </a> </p>'

st.markdown(cl, unsafe_allow_html=True)
st.markdown(nami, unsafe_allow_html=True)
st.markdown(samhsa, unsafe_allow_html=True)
st.markdown(textline, unsafe_allow_html=True)
st.markdown(betterhelp, unsafe_allow_html=True)



