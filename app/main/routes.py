from flask import render_template
from app.main import bp
from flask import current_app

@bp.route('/')
def index():
    return render_template('index.html', streamlit_apps_url=current_app.config['STREAMLIT_APPS_URL'])

@bp.route('/text_editor')
def text_editor():
    return render_template('text_editor.html', streamlit_apps_url=current_app.config['STREAMLIT_APPS_URL'])
