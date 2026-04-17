import jwt
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify, current_app
from ..models.admin import AdminUser

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password required'}), 400

    user = AdminUser.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401

    expiry = datetime.utcnow() + timedelta(hours=current_app.config['JWT_EXPIRY_HOURS'])
    token = jwt.encode(
        {'user_id': user.id, 'exp': expiry},
        current_app.config['SECRET_KEY'],
        algorithm='HS256'
    )

    return jsonify({'token': token, 'user': user.to_dict()})
