"""
Render the Main pages Women, Men and Kids
"""
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp = Blueprint('bp', __name__, template_folder="../template", static_folder="../static")


@bp.route('/',  strict_slashes=False)
def home():
    """
    Render Home page
    :return: HTML Home page
    :raises 404 if the template not found
    """
    try:
        return render_template("index.html", title="Admin-Dashboard")
    except TemplateNotFound:
        abort(404)


@bp.route('/men')
def men():
    """
    Render men page
    :return: HTML men page
    :raises 404 if the template not found
    """
    try:
        return render_template("men.html", title="Admin-dashboard")
    except TemplateNotFound:
        abort(404)


@bp.route('/women')
def women():
    """
    Render women page
    :return: HTML women page
    :raises 404 if the template not found
    """
    try:
        return render_template("women.html", title="Admin-dashboard")
    except TemplateNotFound:
        abort(404)


@bp.route('/admin')
def admin():
    """
    Render kids page
    :return: HTML kids page
    :raises 404 if the template not found
    """
    try:
        return render_template("admin.html")
    except TemplateNotFound:
        abort(404)


@bp.route('/cart')
def cart():
    try:
        return render_template('cart.html')
    except TemplateNotFound:
        abort(404)
