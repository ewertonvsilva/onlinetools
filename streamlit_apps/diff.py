from streamlit_elements import elements, mui, html, lazy, sync, editor
import streamlit as st
from streamlit_ace import st_ace

EDITOR_HEIGHT = 700
st.set_page_config(
    page_title="Diff Editor",
    layout="wide",
    page_icon=':material/edit_note:'
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

with col1:
    # Spawn a new Ace editor
    content_a = st_ace(auto_update=True, language="abc",  min_lines=31, height=EDITOR_HEIGHT-200)   

with col2:
    # Spawn a new Ace editor
    content_b = st_ace(auto_update=True, language="abc",  min_lines=31, height=EDITOR_HEIGHT-199)   

with elements("monaco_editors"):
    editor.MonacoDiff(
        original=content_a,
        modified=content_b,
        height=EDITOR_HEIGHT,
    )



