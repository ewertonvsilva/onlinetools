from streamlit_monaco import st_monaco
import streamlit as st

st.title("Streamlit Markdown Editor")

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'

content = st_monaco(value=st.session_state.key, height="600px", language="markdown")

if st.button("Show editor's content"):
    st.session_state.key = content.upper() + "AHH"