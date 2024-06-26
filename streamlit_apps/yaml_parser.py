import yaml
import json
import streamlit as st
st.set_page_config(page_title='Yaml Parser',layout="wide", page_icon =':material/integration_instructions:' )


col1, col2 = st.columns([0.4,0.6], gap="small")

f = col1.text_area("Yaml Input", height=400) 

yaml_obj = yaml.safe_load(f) 
json_str = json.dumps(yaml_obj)

if not f:
    json_str = json.loads('{}') 

col2.text('Yaml Dump')
col2.json(json_str, expanded=False)
