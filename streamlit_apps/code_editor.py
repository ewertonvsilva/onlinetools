import streamlit as st
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

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
# ----

c1, c2 = st.columns([0.9,0.1], gap="small")

with c2:
    with st.container(border=True):
        language = st.selectbox("Language mode", options=LANGUAGES, index=1)
        tab_size = st.slider("Tab size", 1, 8, 4)

with c1:
    content = st_ace(
                    language=language,
                    font_size=14,
                    tab_size=tab_size,
                    show_gutter= True,
                    wrap=True,
                    auto_update=True,
                    min_lines=45,
                    key="ace",
                )
                
