from flask import Blueprint, jsonify, request, render_template
from ..models import Clothing, Top, Bottom

men = Blueprint('Men', __name__, url_prefix='/api')
Models = [Clothing, Top, Bottom]


@men.route('/men')
def product():
    """
    represent all the available product on the storage
    if there is a query search base on the query if not just search all men cloth
    :return: all product randomly
    """
    try:
        # cloth = Clothing.query
        # top = Top.query
        # bottom = Bottom
        if len(request.args.to_dict()) == 0:
            all_product = Clothing.filterSearch({'category_id': 1}).all()
            # return jsonify([arg.to_dict for arg in all_product])
            return render_template('index.html')

        validParameters = request.args.to_dict()
        query_results = []

        for Model in Models:
            query = Model.query

            for key, value in validParameters.items():
                if hasattr(Model, key):
                    query = query.filter(getattr(Model, key) == value)
            query_results.append(query.all())
        print(query_results)
        return render_template('men.html')


        # return jsonify([arg.to_dict() for arg in products])

    except Exception as e:
        print("Error in men all product routs", e)


# @men.route('/men')
