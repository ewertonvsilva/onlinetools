import yaml
import json
import streamlit as st
from streamlit_ace import st_ace

st.set_page_config(
    page_title="Yaml Parser",
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

# st.set_page_config(page_title='Yaml Parser',layout="wide", page_icon =':material/integration_instructions:' )


col1, col2 = st.columns([0.5,0.5], gap="small")


with col1:
    f = st_ace(auto_update=True, language="yaml",  min_lines=31, height=600) 


yaml_obj = yaml.safe_load(f) 

json_str = json.dumps(yaml_obj)

if not f:
    json_str = json.loads('{}') 

col2.text('Yaml Dump')
col2.json(json_str, expanded=False)
