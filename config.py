import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevConfig:
    STREAMLIT_APPS_URL = {
        "list_to_array": "http://localhost:8501",
        "text_editor": "http://localhost:8502"
    }


class ProdConfig:
    STREAMLIT_APPS_URL = {
        "list_to_array": "https://onlinetools-list-to-array.streamlit.app",
        "text_editor": "https://onlinetools-code-editor.streamlit.app"
    }


config = {"dev": DevConfig, "prod": ProdConfig, "production": ProdConfig}