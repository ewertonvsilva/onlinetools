export FLASK_ENV=dev
hap run -- flask run -h 0.0.0.0 -p 8081 
hap run -- streamlit run streamlit_apps/list_to_array.py --server.port 8501
hap run -- streamlit run streamlit_apps/code_editor.py --server.port 8502
hap run -- streamlit run streamlit_apps/yaml_parser.py --server.port 8503
hap run -- streamlit run streamlit_apps/sql_formatter.py --server.port 8504
hap run -- streamlit run streamlit_apps/json_parser.py --server.port 8505
hap run -- streamlit run streamlit_apps/diff.py --server.port 8506

open http://0.0.0.0:8081
hap status