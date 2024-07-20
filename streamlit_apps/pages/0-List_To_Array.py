import json
import streamlit as st
from streamlit_ace import st_ace

OUTPUT_HEIGHT = 250

st.set_page_config(
    page_title="List to Array",
    layout="wide",
    page_icon=":material/data_array:"
)

margins_css = """
    <style>
        .main > div {
            padding-left: 6rem;
            padding-right: 2rem;
            padding-top: 0rem;
        }
        header {display: none!important;}
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)
# ----

col1, col2, col3 = st.columns([0.41,0.18,0.41], gap="small")

with col1:
    # Spawn a new Ace editor
    content = st_ace(auto_update=True, language="abc",  min_lines=31, height=600)   

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
    python_content_list = content

    if break_line:
        quote_type = '"' if quote=='Double' else "'"
        tmp_content = "[\n"
        tmp_raw_content = ''
        last_c = 0
        for element in python_content_list:
            last_c +=1
            tmp_content +=f" {quote_type}{element}{quote_type}{',' if not (last_c == len(python_content_list)) else ''}\n"  # Add quotes and trailing comma
            tmp_raw_content +=f" {element}{',' if not (last_c == len(python_content_list)) else ''}\n"  # Add quotes and trailing comma


        tmp_content +="]"

        python_content = tmp_content

    with st.container(height=OUTPUT_HEIGHT, border=False):
        st.code(python_content, language='python')

    st.text("Raw")
    raw = ','.join(content)

    if break_line:
         raw = tmp_raw_content

    with st.container(height=OUTPUT_HEIGHT, border=False):
        st.code(raw, language='python')


