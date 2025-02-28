from functools import wraps
from flask import jsonify, session
from ..auth.models import RoleUser, Role


def role_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        userId = session.get('user_id')
        if not userId:
            return jsonify({"error": "You don't have permission you need to login"}), 400

        query = RoleUser.query.filter_by(user_id=userId).first()

        if not query:
            return jsonify({"error": "user isn't registerd"}), 400
        roleCheck = Role.query.filter_by(id=query.role_id).first()

        if not roleCheck or roleCheck.name != 'user':
            return jsonify({"error": "permission denied you dont have access"}), 400

        return func(*args, **kwargs)
    return wrapper
