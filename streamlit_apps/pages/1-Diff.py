import streamlit as st
from streamlit_ace import st_ace
from st_diff_viewer import diff_viewer
from streamlit_option_menu import option_menu

#https://github.com/victoryhb/streamlit-option-menu

EDITOR_HEIGHT = 700
st.set_page_config(
    page_title="Diff Editor",
    layout="wide",
    page_icon=':material/edit_note:'
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




option_menu_sel = option_menu(None, ["Home", "Text Processing", "Parsers", 'Code Formatters'], 
    icons=['Home', 'blockquote-left', "braces", 'code'], 
    menu_icon="cast", default_index=1, orientation="horizontal")


col1, col2 = st.columns([0.5,0.5], gap="small")

with col1:
    # Spawn a new Ace editor
    content_a = st_ace(auto_update=True, language="abc",  min_lines=31, height=EDITOR_HEIGHT-200)   

with col2:
    # Spawn a new Ace editor
    content_b = st_ace(auto_update=True, language="abc",  min_lines=31, height=EDITOR_HEIGHT-199)   

if content_a==content_b:
    st.write("No Difference!")
else:
    st.write("Difference:")

split_view = st.checkbox("Split View", True)


diff_viewer(
    content_a,
    content_b,
    split_view=split_view,
    extra_lines_surrounding_diff=50
)