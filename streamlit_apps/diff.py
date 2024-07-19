# from streamlit_elements import elements, mui, html, lazy, sync, editor
import streamlit as st
from streamlit_ace import st_ace
# import diff_viewer
from st_diff_viewer import diff_viewer



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

col1, col2 = st.columns([0.5,0.5], gap="small")

with col1:
    # Spawn a new Ace editor
    content_a = st_ace(auto_update=True, language="abc",  min_lines=31, height=EDITOR_HEIGHT-200)   

with col2:
    # Spawn a new Ace editor
    content_b = st_ace(auto_update=True, language="abc",  min_lines=31, height=EDITOR_HEIGHT-199)   

# with elements("monaco_editors"):
#     editor.MonacoDiff(
#         original=content_a,
#         modified=content_b,
#         height=EDITOR_HEIGHT,
#     )

if content_a==content_b:
    st.write("No Difference!")
else:
    st.write("Difference:")

# diff_viewer.diff_viewer(old_text=content_a, new_text=content_b, lang='none')

split_view = st.checkbox("Split View", True)


diff_viewer(
    content_a,
    content_b,
    split_view=split_view,
    # use_dark_theme=use_dark_theme,
    # left_title=",
    # right_title=right_title,
    extra_lines_surrounding_diff=50,
    # hide_line_numbers=hide_line_numbers,
    # highlight_lines=highlight_lines,
)