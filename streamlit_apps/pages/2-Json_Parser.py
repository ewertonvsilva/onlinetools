import json
import streamlit as st
from streamlit_ace import st_ace


st.set_page_config(
    page_title="Json Parser",
    layout="wide",
    page_icon=":material/integration_instructions:"
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


col1, col2 = st.columns([0.5,0.5], gap="small")


with col1:
    f = st_ace(auto_update=True, language="json",  min_lines=31, height=600) 

try:
    json_str = json.loads(f or "{}")
except:
    json_str = f

col2.text('Json Parsed')
col2.json(json_str, expanded=False)
