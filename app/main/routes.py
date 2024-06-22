from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/text_editor')
def text_editor():
    return render_template('text_editor.html')
