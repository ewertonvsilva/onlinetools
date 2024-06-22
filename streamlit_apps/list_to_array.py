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
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.3,0.2,0.5], gap="small")

with col1:
    # Spawn a new Ace editor
    content = st_ace(auto_update=True, language="abc",  min_lines=30)   

with con2:
    quote = st.radio("Quotes", ['Simple', 'Double'])
    on_empty = st.toggle("Ignore Empty Line")
    break_line = st.toggle("Break Line")
    set_case = st.radio("Case", ['As Source', 'Upper', 'Lower'])

with col3:
    # scol1, scol2, scol3 = st.columns(3, gap="small")
    # with scol1:
        
    # with scol3:
    #     on_empty = st.toggle("Ignore Empty Line")
    #     break_line = st.toggle("Break Line")
    # with scol2:
    #     set_case = st.radio("Case", ['As Source', 'Upper', 'Lower'])

    # st.divider()

    st.text("Pyhton / js")
    content = content.split('\n')

    content = [x.replace('\r', '') for x in content]

    if on_empty:
        content = list(filter(str.strip, content))
    
    if set_case=='Upper':
        content = [x.upper() for x in content]

    if set_case=='Lower':
        content = [x.lower() for x in content]
    
    python_content = str(content).replace("'",'"') if quote=='Double' else content

    if break_line:
        python_content = str(python_content).replace(',',',\n')
        join_char = ''

    st.code(python_content, language='python')

    st.text("Raw")
    raw = ','.join(content)

    if break_line:
         raw = ','.join(content).replace(',',',\n')

    st.code(raw, language='python')


