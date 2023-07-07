import streamlit as st

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")
fp = st.sidebar.file_uploader("hello") 

text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)