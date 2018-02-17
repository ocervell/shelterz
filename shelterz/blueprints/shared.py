from flask import Blueprint, render_template, current_app

bp = Blueprint('shared', templates='templates')

@bp.route('/')
def index():
    return render_template('index.html', settings=current_app.config)
