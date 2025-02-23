"""
routs belong to men products that client could use
"""
import json
from flask import Blueprint, jsonify, request, render_template
from ..models import Clothing, Top, Bottom
from ..utils.helper import TopOrBottom, checkCorrectParameter

men = Blueprint('Men', __name__, url_prefix='/api')
Models = [Clothing, Top, Bottom]


@men.route('/men')
def product():
    """
    represent all the available product on the storage
    if there is a query search base on the query if not just search all men cloth
    :return: all product randomly
    """
    from app import db
    try:
        if checkCorrectParameter(list(request.get_json()), lst=["length", "sleeve", "color", "company", "gender"]):

            if len(request.get_json()) == 0:

                all_product = Clothing.query.all()
                result = [arg.to_dict() for arg in all_product]
                return json.dumps(result, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2), 200

            holder = request.get_json()
            if TopOrBottom(holder) == "top":

                query = db.session.query(Clothing). \
                    join(Top, Top.clothing_id == Clothing.id, isouter=True).filter(Top.sleeve.isnot(None)).all()
                result = [arg.to_dict() for arg in query]
                return json.dumps(result, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2), 200

            query = db.session.query(Clothing). \
                join(Bottom, Bottom.clothing_id == Clothing.id, isouter=True).filter(Bottom.length.isnot(None)).all()
            result = [arg.to_dict() for arg in query]
            return json.dumps(result, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2), 200

        return jsonify({"error": "Wrong parameter name used for retrieving data"})

    except Exception as e:
        return jsonify({"error": f"Cannot retrieve data because of {e}"}), 400
