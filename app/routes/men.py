from flask import Blueprint, jsonify, request, render_template
from ..utils.help import conectModel
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
        print(validParameters)
        query = None
        for Mchek in Models:
            print('2 level above')
            for ky, val in validParameters.items():
                print('1 level aboce')
                if hasattr(Mchek, ky):
                    print('deep')
                    query = Mchek.filterSearch((ky, val))
                    print(query)
        print("this is ", query)
        return render_template('men.html')


        # return jsonify([arg.to_dict() for arg in products])

    except Exception as e:
        print("Error in men all product routs", e)


# @men.route('/men')
