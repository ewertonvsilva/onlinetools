import json
import streamlit as st
from streamlit_ace import st_ace

st.set_page_config(
    page_title="List to Array",
    layout="wide"
)

margins_css = """
    <style>
        .main > div {
            padding-left: 1rem;
            padding-right: 2rem;
            padding-top: 0rem;
        }
        header {display: none!important;}
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.41,0.18,0.41], gap="small")

with col1:
    # Spawn a new Ace editor
    content = st_ace(auto_update=True, language="abc",  min_lines=30)   

with col2:
    with st.container(border=True):
        quote = st.radio("Quotes", ['Simple', 'Double'])
        set_case = st.radio("Case", ['As Source', 'Upper', 'Lower'])
        on_empty = st.toggle("Ignore Empty Line")
        break_line = st.toggle("Break Line")
        on_duplicates = st.toggle("Remove Duplicates")
        on_sort = st.toggle("Sort Items")
        

with col3:

    st.text("Pyhton / js")
    content = content.split('\n')

    content = [x.replace('\r', '') for x in content]

    if on_empty:
        content = list(filter(str.strip, content))
    if on_duplicates:
        content  = list(set(content))

    if on_sort:
        content.sort()

    if set_case=='Upper':
        content = [x.upper() for x in content]

    if set_case=='Lower':
        content = [x.lower() for x in content]
    
    python_content = str(content).replace("'",'"') if quote=='Double' else content

    if break_line:
        python_content = str(python_content).replace(',',',\n')
        join_char = ''

    with st.container(height=200, border=False):
        st.code(python_content, language='python')

    st.text("Raw")
    raw = ','.join(content)

    if break_line:
         raw = ','.join(content).replace(',',',\n')

    with st.container(height=200, border=False):
        st.code(raw, language='python')


