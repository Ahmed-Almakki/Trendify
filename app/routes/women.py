"""
routs belong to women products that client could use
"""
import json
from flask import Blueprint, jsonify, request
from ..models import Clothing, Top, Bottom
from ..utils.helper import TopOrBottom, checkCorrectParameter

women = Blueprint('Women', __name__, url_prefix='/api')
Models = [Clothing, Top, Bottom]


@women.route('/women')
def Wproduct():
    """
    represent all the available product on the storage
    if there is a query search base on the query if not just search all men cloth
    :return: all product randomly
    """
    from app import db
    try:

        if not request.is_json:

            all_product = Clothing.query.filter(Clothing.gender == 'women').all()
            result = [arg.to_dict() for arg in all_product]
            return json.dumps(result, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2), 200

        elif checkCorrectParameter(list(request.get_json()), lst=["length", "sleeve", "color", "company", "gender"]):
            holder = request.get_json(silent=True)
            query = db.session.query(Clothing)
            filter_list = [Clothing.gender != 'men']

            if TopOrBottom(holder) == "top":

                query = query(Clothing). \
                    join(Top, Top.clothing_id == Clothing.id, isouter=True)

                for key, val in holder.items():
                    if hasattr(Clothing, key):
                        filter_list.append(getattr(Clothing, key) == val)
                    else:
                        filter_list.append(getattr(Top, key) == val)

                query = query.filter(*filter_list).all()
                result = [arg.to_dict() for arg in query]
                return json.dumps(result, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2), 200

            query = db.session.query(Clothing). \
                join(Bottom, Bottom.clothing_id == Clothing.id, isouter=True)
            for key, val in holder.items():
                if hasattr(Clothing, key):
                    filter_list.append(getattr(Clothing, key) == val)
                else:
                    filter_list.append(getattr(Bottom, key) == val)

            query = query.filter(*filter_list).all()
            result = [arg.to_dict() for arg in query]
            if len(result) == 0:
                return jsonify({"Warning": "No product found meeting the criteria"}), 404
            return json.dumps(result, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2), 200

        return jsonify({"error": "Wrong parameter name used for retrieving data"})

    except Exception as e:
        return jsonify({"error": f"Cannot retrieve data because of {e}"}), 400
