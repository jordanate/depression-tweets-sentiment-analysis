import streamlit as st

st.title('Depression in Tweets Detector')

st.text('Type a tweet')

n = st.number_input('Number', step=1)

st.write('Possibility of Depression?')
st.write(f'{n} + 1 = {n+1}')

s = st.text_input('Type a name in the box below')

st.write(f'Hello {s}')