"""
Render the Main pages Women, Men and Kids
"""
from flask import Blueprint

bp = Blueprint('bp', __name__, template_folder="/template", static_folder="/static")

@bp.route('/')
def welcom():
    """
    render the welcome page route
    :return:
    """