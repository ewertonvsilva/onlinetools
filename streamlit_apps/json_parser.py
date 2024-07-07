import json
import streamlit as st

st.set_page_config(
    page_title="Json Parser",
    layout="wide",
    page_icon=":material/integration_instructions:"
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


col1, col2 = st.columns([0.5,0.5], gap="small")

f = col1.text_area("Json Input", height=700) 

#yaml_obj = yaml.safe_load(f) 
json_str = json.loads(f or "{}")

# if not f:
#     json_str = json.loads('{}') 

col2.text('Json Parsed')
col2.json(json_str, expanded=False)
