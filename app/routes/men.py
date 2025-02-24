"""
routs belong to men products that client could use
"""
import json
from flask import Blueprint, jsonify, request
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

        # check if the request contain a json if not show all the cloth relate to men
        if not request.is_json:

            # query all the product relate to men
            all_product = Clothing.query.filter(Clothing.gender != 'women').all()
            result = [arg.to_dict() for arg in all_product]

            # json .dumps because the result list contain dict which have unserizable objct
            return json.dumps(result, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2), 200

        elif checkCorrectParameter(list(request.get_json()), lst=["length", "sleeve", "color", "company", "gender"]):
            holder = request.get_json(silent=True)
            query = db.session.query(Clothing)
            filter_list = [Clothing.gender != 'women']

            if TopOrBottom(holder) == "top":

                # query using Top and Clothing Models
                query = query.\
                    join(Top, Top.clothing_id == Clothing.id, isouter=True)

                # loop over all the dict
                for key, val in holder.items():

                    # check if one of the key belong to Clothing Model if so
                    if hasattr(Clothing, key):

                        # getattr(clothing, key) ==> Clothing.Length
                        # getattr(clothing, key) == val --> Clothing.Length == val (short)
                        # add the condition to filter list to filter it
                        filter_list.append(getattr(Clothing, key) == val)
                    else:
                        filter_list.append(getattr(Top, key) == val)

                query = query.filter(*filter_list).all()
                result = [arg.to_dict() for arg in query]
                return json.dumps(result, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2), 200

            # query using the Bottom and Clothing Models
            query = db.session.query(Clothing). \
                join(Bottom, Bottom.clothing_id == Clothing.id, isouter=True)
            for key, val in holder.items():
                if hasattr(Clothing, key):
                    filter_list.append(getattr(Clothing, key) == val)
                else:
                    filter_list.append(getattr(Bottom, key) == val)

            # using *cond because using cond without astrickt raise error, you need to unpack it
            # and because it is a list just use one astrikt
            query = query.filter(*filter_list).all()
            result = [arg.to_dict() for arg in query]
            return json.dumps(result, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2), 200

        return jsonify({"error": "Wrong parameter name used for retrieving data"})

    except Exception as e:
        return jsonify({"error": f"Cannot retrieve data because of {e}"}), 400
