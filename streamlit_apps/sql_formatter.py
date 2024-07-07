import streamlit as st
import sqlparse

st.set_page_config(
    page_title="SQL Formater",
    layout="wide",
    page_icon=":material/join_inner:"
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

# st.set_page_config(page_title='SQL Formater', layout="wide", page_icon=':material/join_inner:')


col1, col2 = st.columns([0.4,0.6], gap="small")

in_code = col1.text_area("SQL Query", height=400)
out_code = sqlparse.format(in_code, reindent=True, keyword_case='upper')
col2.text('Formated Query')
col2.code(out_code, language="sql", line_numbers=True)
