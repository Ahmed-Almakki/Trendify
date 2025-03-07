"""
authentication and authorization
"""
from flask import Blueprint, render_template, request, jsonify, session
from flask_security.utils import hash_password, verify_password
from ..auth.models import User, Role
from app import user_datastore, db


auth = Blueprint('auth', __name__, template_folder='template')


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        try:
            if not request.form:
                return jsonify({"error": "Missing Registration data"}), 404

            password = request.form['password']
            username = request.form['name']
            email = request.form['email']

            if not username or not email or not password:
                return jsonify({"error": "All field are required"}), 404

            if user_datastore.find_user(email=email):
                return jsonify({"error": "user already exists"}), 400

            user = user_datastore.create_user(password=hash_password(password), name=username, active=False, email=email)

            # search the Role table for a new person who register
            # because he is already register he well not has a role so the filter well choose him
            # and assign the role user to him

            role = Role.query.filter_by(name='user').first()
            if not role:
                role = Role(name="user", description="default user role description")
                db.session.add(role)
                db.session.commit()

            # add the role to user
            user_datastore.add_role_to_user(user, role)
            db.session.commit()
            return jsonify({"message": "Created user successfully"}), 201
        except Exception as e:
            return jsonify({"error": f"Cannot create account due to {e}"}), 400


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        try:
            if not request.form:
                return jsonify({"error": "Missing data login"}), 404

            password = request.form['password']
            email = request.form['email']

            if not email or not password:
                return jsonify({"error": "need password and email"}), 404

            user = User.query.filter_by(email=email).first()
            if not user:
                return jsonify({"error": "user is not registered"}), 400

            if not verify_password(password, user.password):
                return jsonify({"error": "wrong password"})

            session['user_id'] = user.id
            session.modified = True
            print("session is ", session)
            return jsonify({"message": "successfully logged in"}), 200
        except Exception as e:
            return jsonify({"error": f"cannot logged in due to {e}"})
