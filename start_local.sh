export FLASK_ENV=dev
hap run -- flask run -h 0.0.0.0 -p 8081 
hap run -- streamlit run streamlit_apps/list_to_array.py --server.port 8501
hap run -- streamlit run streamlit_apps/code_editor.py --server.port 8502


open http://0.0.0.0:8081
hap status