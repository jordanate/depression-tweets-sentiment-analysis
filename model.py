import streamlit as st

model = pickle.load(open('model3.pkl','rb'))

st.title('Depression in Tweets Detector')

n = st.number_input('Type a tweet', step=1)

st.write('Possibility of Depression?')

st.write(f'{n}')