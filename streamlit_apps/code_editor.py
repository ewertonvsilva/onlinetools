import streamlit as st
from streamlit_monaco import st_monaco

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
#-- 

# - Persist editor content across executions:
if 'changed_content' not in st.session_state:
	st.session_state.changed_content = ''

c1, c2 = st.columns([0.8,0.2], gap="small")

with c1:
    content = st_monaco(
                    value=st.session_state.changed_content,
                    language=c2.selectbox("Language mode 2", options=['Python'], index=0),
                    # font_size=14,
                    # tab_size=tab_size,
                    # show_gutter= True,
                    # wrap=True,
                    # auto_update=True,
                    # min_lines=45,
                    # key="ace",
                )
with c2:
    # with st.container(border=True):
    #     language = st.selectbox("Language mode", options=['Python'], index=0)
    #     tab_size = st.slider("Tab size", 1, 8, 4)
    if st.button("Upper Case"):
        st.session_state.changed_content = content.upper()