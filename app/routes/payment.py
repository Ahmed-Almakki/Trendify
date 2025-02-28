from flask import session, Blueprint, request, jsonify, redirect, url_for, render_template
from ..models import Clothing, Top, Bottom

payment = Blueprint('payment', __name__)


@payment.route('/checkSession')
def checkSession():
    print("jhgjhghgjgjghj")
    return jsonify({"session": session['user_id']})


@payment.route('/set_email', methods=['POST', 'GET'])
def setCart():
    """
    when customer click add to cart it suppose to be redirected to page with just email
    so when he enters email we create a session based on his email so every time he add
    product to the cart to be added to his email session
    :return: redirect to cart page when post request, and email page when get
    """
    if request.method == 'POST':
        session['cart'] = request.form['email']
        print(session, '\n', session.get('cart'))
        return redirect(url_for('.addToCart'))
    return render_template('email.html')


@payment.route('/delete_email')
def deleteEmail():
    """
    delete product from the cart "just delete session or just pop"
    :return:
    """
    session.pop('cart', default=None)
    return jsonify({"message": "product deleted successfully"}), 200


@payment.route('/add')
def addToCart():
    """
    add product to cart "session"
    :return:
    """
    try:
        # print(session, '\n', session.keys(), '\n', session.get('cart'))
        if not session.get('cart'):
            return redirect(url_for('.setCart'))
        cloth_id = request.args.get('cloth_id')
        quantity = int(request.form['quantity'])
        if not cloth_id or not quantity:
            return jsonify({"error": "Missing cloth id or count"}), 400

        cloth = Clothing.query.filter_by(id=cloth_id).first()
        if not cloth:
            return jsonify({"error": "Cloth not found"}), 404

        item = {'price': cloth.price, 'quantity': quantity, 'total_price': int(cloth.price) * quantity}
        # check if there is an existing cart "session"
        cart_id = 'cart.' + str(cloth.id)
        checkItemExist = session.get(cart_id)
        # putting "creating" product in cart because not exist "first item client buy"
        if not checkItemExist:
            session[cart_id] = {}
            print("ahmed")
            for key, val in item.items():
                session[cart_id][key] = val
        # client already bought stuff and wanted more
        else:
            old_quantity = session[cart_id]['quantity']
            new_quantity = old_quantity + quantity
            old_price = session[cart_id]['total_price']
            new_price = (int(cloth.price) * new_quantity)
            session[cart_id]['quantity'] = new_quantity
            session[cart_id]['total_price'] = new_price

        print(session, '\n', session['cart'])
        return jsonify({"message": "true"})
    except Exception as e:
        return jsonify({"error": f"error due to {e}"})