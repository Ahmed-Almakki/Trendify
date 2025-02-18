from flask import Blueprint, jsonify
from ..models import Clothing


men = Blueprint('Men', __name__, url_prefix='/api')


@men.route('/product')
def product():
    """
    represent all the available product on the storage
    :return: all product randomly
    """
    try:
        cloth = Clothing.query.all()
        return jsonify([clothing.to_dict() for clothing in cloth])
    except Exception as e:
        print("Error in men product routs", e)
