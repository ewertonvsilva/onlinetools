import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="dailytasks.tools",
    layout="wide",
    page_icon=":material/construction:"
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
    menu_icon="cast", default_index=0, orientation="horizontal")


st.write("# Daily Tasks Tools")

col1, col2 = st.columns([0.5,0.5], gap="small")

col1.markdown(
"""
## Text Processing
- [Diff Text](Diff)
- [List to Array](List_To_Array)

## Parsers
- [Yaml Parser](Yaml_Parser)
- [Json Parser](Json_Parser)
"""
)

col2.markdown(
"""
## Code Formatters
- [SQL Formatter](Sql_Formatter)
"""
)