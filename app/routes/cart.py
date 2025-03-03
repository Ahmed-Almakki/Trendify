"""
contain function that deals with cart adding - delete - update
"""
from flask import session, Blueprint, request, jsonify, redirect, url_for, render_template
import stripe
from ..models import Clothing, Top, Bottom

cart = Blueprint('payment', __name__)


@cart.route('/checkSession')
def checkSession():
    print("jhgjhghgjgjghj")
    return jsonify({"session": session['user_id']})


@cart.route('/set_email', methods=['POST', 'GET'])
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


@cart.route('/delete_email')
def deleteEmail():
    """
    delete product from the cart "just delete session or just pop"
    :return:
    """
    session.pop('cart', default=None)
    return jsonify({"message": "product deleted successfully"}), 200


@cart.route('/add')
def addToCart():
    """
    add product to cart "session"
    :return: json message
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
            new_price = (int(cloth.price) * new_quantity)
            session[cart_id]['quantity'] = new_quantity
            session[cart_id]['total_price'] = new_price
        print(session, '\n', session['cart'])
        return jsonify({"message": "item successfully added to cart"}), 201
    except Exception as e:
        return jsonify({"error": f"error due to {e}"})
    

@cart.route('/delCart', methods=['DELETE'])
def deleteFromCart():
    """
    delete specific item from cart
    :return: json message 
    """
    try:
        cloth_id = request.args.get('cloth_id')
        if not cloth_id:
            return jsonify({"error": "Missing cloth_id parameter"}), 400
        
        item = 'cart.' + str(cloth_id)
        cloth = session.get(item)
        if not item:
            return jsonify({"error": "item isn't in cart"}), 400
        
        session.pop(item)
        print(session)
        return jsonify({"message": "deleted successfully from cart"}), 200
    except Exception as e:
        return jsonify({"error": f"Can't delete item from cart due to {e}"}), 400


@cart.route('/create-checkout', methods=['POST'])
def createCheckout():
    try:
        if not session.get('cart'):
            return redirect(url_for('.setCart'))

        line_item = []
        for key in session.keys():
            if key.startswith('cart.'):
                item = session[key]
                line_item.append({
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': key.split('.')[1],
                        },
                        'unit_amount': int(item['price'])
                    },
                    'quantity': item['quantity'],
                })

        if not line_item:
            return jsonify({"error": "No item found in cart"}), 400
        print(line_item)

        checkoutSession = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_item,
            mode='payment',
            success_url=url_for('.success', _external=True),
            cancel_url=url_for('.cancel', _external=True),
        )
        return jsonify({"url": checkoutSession.url})
    except Exception as e:
        return jsonify({"error": f"Can't checkout due to {e}"}), 400


@cart.route('/checkout/success')
def success():
    return jsonify({"message": "Payment successful! Thank you for your purchase."}), 200


@cart.route('/checkout/cancel')
def cancel():
    return jsonify({"messae": "Payment cancelled. Your cart is still saved."}), 400
