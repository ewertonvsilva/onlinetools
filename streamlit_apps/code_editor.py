import streamlit as st
from streamlit_monaco import st_monaco

st.set_page_config(
    page_title="Code Editor",
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

if 'content' not in st.session_state:
	st.session_state.content = ''

if 'previous' not in st.session_state:
	st.session_state.previous = ''

#--
def add_prefix(text, prefix):
    lines = text.splitlines()
    prefixed_lines = [prefix + line for line in lines]
    return "\n".join(prefixed_lines)

def add_sufix(text, sufix):

  lines = text.splitlines()
  prefixed_lines = [line + sufix for line in lines]
  return "\n".join(prefixed_lines)

def set_add_sufix():
    if st.session_state.content:
        st.session_state.previous = st.session_state.content
        st.session_state.changed_content = add_sufix(st.session_state.content, st.session_state.widget_sufix)
        st.session_state.widget_sufix = ""

def set_add_prefix(prefix):
    if st.session_state.content:
        st.session_state.previous = st.session_state.content
        st.session_state.changed_content = add_prefix(st.session_state.content, prefix)
        # st.session_state.widget_prefix= ""
#--
col1, col2 = st.columns([0.75,0.25], gap="small")


with col2:
    btc1, btc2, btc3 = st.columns([0.24,0.38,0.38], gap='small')

    with btc3:
        if st.button("⬆ Upper"):
            st.session_state.previous = st.session_state.content
            st.session_state.changed_content = st.session_state.content.upper()
    
    with btc2:
        if st.button("⬇ Lower"):
            st.session_state.previous = st.session_state.content
            st.session_state.changed_content = st.session_state.content.lower()

    with btc1:
        if st.button("🔙"):
            st.session_state.changed_content = st.session_state.previous

    # -- replace
    with st.form("replace_form", clear_on_submit=True):
        colfr1,colfr2,colfr3 = st.columns(3, gap="small")

        replace_from = colfr1.text_input('from', placeholder='From', label_visibility='collapsed')
        replace_to =  colfr2.text_input('to', placeholder='To',label_visibility='collapsed')
        submitted_replace = colfr3.form_submit_button('Replace')

        if submitted_replace and st.session_state.content:
            st.session_state.previous = st.session_state.content
            st.session_state.changed_content = st.session_state.content.replace(replace_from, replace_to)

    # -- prefix
    with st.form("prefix_form", clear_on_submit=True):
        colp1,colp2 = st.columns([2,1], gap="small")

        prefix = colp1.text_input('', placeholder='Prefix', label_visibility='collapsed')
        submitted_prefix = colp2.form_submit_button('Add prefix')

        if submitted_prefix and st.session_state.content:
            st.session_state.previous = st.session_state.content
            st.session_state.changed_content = add_prefix(st.session_state.content, prefix)

    # -- sufix
    with st.form("sufix_form", clear_on_submit=True):
        colp1,colp2 = st.columns([2,1], gap="small")

        sufix = colp1.text_input('', placeholder='sufix', label_visibility='collapsed')
        submitted_sufix = colp2.form_submit_button('Add Sufix')

        if submitted_sufix and st.session_state.content:
            st.session_state.suvious = st.session_state.content
            st.session_state.changed_content = add_sufix(st.session_state.content, sufix)

    #st.text_input("Add prefix", key="widget_prefix", on_change=set_add_prefix)

    # st.text_input("Add sufix", key="widget_sufix", on_change=set_add_sufix)


with col1:
    st.session_state.content = st_monaco(
                        value=st.session_state.changed_content,
                        language='python',
                        height=700
                    )





