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

col1, c2 = st.columns([0.8,0.2], gap="small")


with col1:
    # Spawn a new Ace editor
    #content = st_ace(auto_update=True, language="abc",  min_lines=31, height=600)   
    content = st_ace(
                language=c2.selectbox("Language mode", options=LANGUAGES, index=121),
                theme=c2.selectbox("Theme", options=THEMES, index=35),
                keybinding=c2.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
                font_size=c2.slider("Font size", 5, 24, 14),
                tab_size=c2.slider("Tab size", 1, 8, 4),
                show_gutter=c2.checkbox("Show gutter", value=True),
                show_print_margin=c2.checkbox("Show print margin", value=False),
                wrap=c2.checkbox("Wrap enabled", value=False),
                auto_update=c2.checkbox("Auto update", value=False),
                readonly=c2.checkbox("Read-only", value=False),
                min_lines=45,
                key="ace",
            )
            
