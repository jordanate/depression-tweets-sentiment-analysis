import streamlit as st
import pickle

with open('model_pkl' , 'rb') as f:
    lr = pickle.load(f)

st.title('Depression in Tweets Detector')

n = st.number_input('Type a tweet', step=1)

st.write('Possibility of Depression?')

st.write(f'{n}')